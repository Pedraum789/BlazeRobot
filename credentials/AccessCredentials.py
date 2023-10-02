import requests
import json

BASIC_TOKEN = "ZmYwMWFiN2QtMjQ5Ni00ZDYwLThmYjctMjI3YmIyYWIyZjZkOjczNTNhYzhkLTgyOWQtNDIwZS1iZTZlLTU0YWMxOTA3MDllZg=="
CLIENT_ID = "ff01ab7d-2496-4d60-8fb7-227bb2ab2f6d"
CLIENT_SECRET = "7353ac8d-829d-420e-be6e-54ac190709ef"

def getAcessToken():
    url = 'https://api-sec-vlc.hotmart.com/security/oauth/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'.format(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic {basic_toke}'.format(basic_toke=BASIC_TOKEN)}
    req = requests.post(url, headers=headers)

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        return objeto_json['access_token']

    return ''
