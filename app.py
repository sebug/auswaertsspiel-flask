import os.path
import os
import requests
import srfapi
from requests.auth import HTTPBasicAuth

from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

app.add_url_rule('/otherapi', view_func = srfapi.otherapi)

@app.route("/")
def hello():
    return "Ohai from CI overridden trigger, with an update."

@app.route("/envo")
def envo():
    the_message = os.environ.get("ENVO")
    if (the_message == None):
        the_message = "Not yet defined"
    return the_message

@app.route("/players")
def players():
    player_list = ['Marco Wölfli', 'Saidy Janko']
    return render_template('players.html', player_list = player_list)    

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory('js', path)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('css', path)
