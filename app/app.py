from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"Hello from my CI/CD pipeline! Deployed at {datetime.datetime.now()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)