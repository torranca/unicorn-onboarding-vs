import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv('JPM_CLIENT_ID')
CLIENT_SECRET = os.getenv('JPM_CLIENT_SECRET')

AUTH_URL = 'https://id.payments.jpmorgan.com/am/oauth2/alpha/access_token'

def get_access_token():
    data = {
        'grant_type': 'client_credentials',
        'scope': 'jpm:payments:sandbox',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(AUTH_URL, data=data, headers=headers)
    response.raise_for_status()
    return response.json()['access_token']