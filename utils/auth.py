import requests
import json


class Auth:
    URL = "https://restful-booker.herokuapp.com/auth"

    credentials = json.dumps({
        "username" : "admin",
        "password" : "password123"
    })

    headers = {
        'Content-Type': 'application/json'
    }

    # response = requests.request("POST", url, headers=headers, data=payload)


    def get_token(self):
        response = requests.post(self.URL, headers=self.headers, data = self.credentials)
        print(response.text)
        print(response.json()["token"])