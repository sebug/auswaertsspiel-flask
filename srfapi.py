import os.path
import os
import requests
from requests.auth import HTTPBasicAuth

def otherapi():
    access_token_url = 'https://api.srgssr.ch/oauth/v1/accesstoken?grant_type=client_credentials'
    client_id = os.environ.get('SRG_CONSUMER_KEY')
    client_secret = os.environ.get('SRG_CONSUMER_SECRET')
    r = requests.post(access_token_url, auth=HTTPBasicAuth(client_id, client_secret))
    res = r.json()
    print(res)
    return res['api_product_list']
