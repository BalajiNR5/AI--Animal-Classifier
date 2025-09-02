import os
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.environ.get("AIzaSyBDC4GqkBN7TkSM5ttpsg2YFA-mifI9y8k"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
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
