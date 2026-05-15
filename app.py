import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running!  12345 zxy"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
