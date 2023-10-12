import requests
import json

BASIC_TOKEN_HOTMART = "ZmYwMWFiN2QtMjQ5Ni00ZDYwLThmYjctMjI3YmIyYWIyZjZkOjczNTNhYzhkLTgyOWQtNDIwZS1iZTZlLTU0YWMxOTA3MDllZg=="
CLIENT_ID_HOTMART = "ff01ab7d-2496-4d60-8fb7-227bb2ab2f6d"
CLIENT_SECRET_HOTMART = "7353ac8d-829d-420e-be6e-54ac190709ef"

PUBLIC_KEY_EDUZZ = "24746949"
API_KEY_EDUZZ = "8cc421bbf0df554f735b5f801548401ec126037f53b84f558f657a59bd97de9a"
EMAIL_EDUZZ = "pedraum789@gmail.com"

def getAcessTokenHotmart():
    url = ('https://api-sec-vlc.hotmart.com/security/oauth/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
           .format(client_id=CLIENT_ID_HOTMART, client_secret=CLIENT_SECRET_HOTMART))
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Basic {basic_toke}'.format(basic_toke=BASIC_TOKEN_HOTMART)}
    req = requests.post(url, headers=headers)

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        return objeto_json['access_token']

    return ''

def getAcessTokenEduzz():
    url = ('https://api2.eduzz.com/credential/generate_token?publickey={public_key}&apikey={api_key}&email={email}'
           .format(public_key=PUBLIC_KEY_EDUZZ, api_key=API_KEY_EDUZZ, email=EMAIL_EDUZZ))
    req = requests.post(url)

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        return objeto_json['data']['token']

    return ''