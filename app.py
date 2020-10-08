from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Ohai from CI overridden trigger, with an update."

@app.route("/players")
def players():
    return render_template('players.html')
