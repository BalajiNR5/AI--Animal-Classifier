from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        # Check if file exists
        if "image" in request.files:
            image_file = request.files["image"]
            image_path = os.path.join("static", image_file.filename)
            image_file.save(image_path)

            # Process image with Gemini
            response = model.generate_content([
                "Describe this animal and its characteristics.",
                {"mime_type": "image/jpeg", "data": open(image_path, "rb").read()}
            ])
            return jsonify({"response": response.text})

        # If text prompt
        data = request.json
        user_prompt = data.get("prompt", "")
        if not user_prompt.strip():
            return jsonify({"error": "Empty prompt"}), 400

        response = model.generate_content(user_prompt)
        return jsonify({"response": response.text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
