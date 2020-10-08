import os.path
import os
import requests
from requests.auth import HTTPBasicAuth

from flask import Flask, render_template, request, send_from_directory
app = Flask(__name__)

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

@app.route("/otherapi")
def otherapi():
    access_token_url = 'https://api.srgssr.ch/oauth/v1/accesstoken?grant_type=client_credentials'
    client_id = os.environ.get('SRG_CONSUMER_KEY')
    client_secret = os.environ.get('SRG_CONSUMER_SECRET')
    r = requests.post(access_token_url, auth=HTTPBasicAuth(client_id, client_secret))
    res = r.json()
    print(res)
    return res['api_product_list']
    

@app.route("/js/<path:path>")
def send_js(path):
    return send_from_directory('js', path)

@app.route("/css/<path:path>")
def send_css(path):
    return send_from_directory('css', path)
