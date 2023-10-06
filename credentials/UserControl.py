import requests
import json


class UserControl:

    def __init__(self, email):
        self.email = email
    def callRequest(self, url):
        req = requests.post(url, json={'email': self.email})

        if req.status_code == 200:
            return True
        return False

    def userUsing(self):
        return self.callRequest('https://2kpqszdcjcpewunpbtguen6aru0vntne.lambda-url.us-east-1.on.aws/')

    def userNotUsing(self):
        return self.callRequest('https://bo5vbmb4pntjmcbuhl4qfhax6q0fvdgv.lambda-url.us-east-1.on.aws/')
