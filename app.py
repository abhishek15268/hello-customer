from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello, consumer! 👋"

@app.get("/healthz")
def healthz():
    return jsonify({"status": "ok"})

# A tiny function so we have something to unit test
def add(a, b):
    return a + b

if __name__ == "__main__":
    # Local dev server
    app.run(host="127.0.0.1", port=5000, debug=True)
