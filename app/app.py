from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "</p>It is working</p>"
