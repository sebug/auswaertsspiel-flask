import os.path

from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

@app.route("/")
def hello():
    return "Ohai from CI overridden trigger, with an update."

@app.route("/players")
def players():
    return render_template('players.html')

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory('js', path)

