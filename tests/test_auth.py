import requests
from utils.auth import Auth

def test_auth():
        auth = Auth()
        auth.get_token()
