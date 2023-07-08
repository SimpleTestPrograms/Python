import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome..!"

@app.route('/whoami')
def hello():
    return 'Know about me in here: https://www.linkedin.com/in/itsmegaffoor/'

if __name__ == "main":
    app.run(host="0.0.0.0", port=8080)

