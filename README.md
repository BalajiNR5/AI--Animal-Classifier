<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>README - Gemini Flask UI</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 20px;
      max-width: 900px;
      background: #f8f9fa;
      color: #212529;
    }
    h1, h2, h3 {
      color: #0056b3;
    }
    code, pre {
      background: #e9ecef;
      padding: 4px 6px;
      border-radius: 5px;
      font-size: 0.95em;
    }
    pre {
      padding: 12px;
      overflow-x: auto;
    }
    .container {
      background: white;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>🐍 Gemini Flask Image Classifier</h1>
    <p>This project is a simple <strong>Flask web app</strong> integrated with the <strong>Gemini API</strong> for <em>image classification</em>. It allows users to upload an image (e.g., cat, dog, elephant) and receive AI-powered predictions with a modern UI.</p>

    <h2>📂 Repository Structure</h2>
    <pre>
/ (root)
│── app.py              # Main Flask application
│── requirements.txt    # Dependencies
│── vercel.json         # Vercel deployment config
│── runtime.txt         # Python runtime version
│── /templates
│     └── index.html    # Frontend HTML UI
│── /static
│     ├── cat.jpg
│     ├── dog.jpg
│     ├── elephant.jpg
    </pre>

    <h2>⚙️ Installation</h2>
    <pre>
# Clone the repository
git clone https://github.com/yourusername/gemini-flask-ui.git
cd gemini-flask-ui

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
    </pre>

    <h2>🚀 Running the App Locally</h2>
    <pre>
flask run
    </pre>
    <p>Now, open <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a> in your browser.</p>

    <h2>🧠 Powered by Gemini API</h2>
    <p>The app uses <code>Gemini Vision API</code> to analyze uploaded images and return robust, AI-driven predictions.</p>

    <h2>🌐 Deployment on Vercel</h2>
    <p>To deploy the project on <strong>Vercel</strong>:</p>
    <pre>
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
    </pre>

    <h2>✅ Features</h2>
    <ul>
      <li>📸 Upload and classify images (cats, dogs, elephants, etc.)</li>
      <li>🎨 Modern UI with clean design</li>
      <li>⚡ Fast Gemini API integration</li>
      <li>☁️ Easy deployment on Vercel</li>
    </ul>

    <h2>📜 License</h2>
    <p>This project is licensed under the MIT License.</p>
  </div>
</body>
</html>
