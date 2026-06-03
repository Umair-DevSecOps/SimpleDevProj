import os
from flask import Flask


app = Flask(__name__)

@app.route("/fail")
def fail():
    return 1 / 0

@app.route("/")
def home():
    return "App is running! 123456"

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(host="0.0.0.0", port=port)
