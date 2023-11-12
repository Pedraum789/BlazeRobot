import requests
import json

def getLastIdHistory():
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        return objeto_json['records'][0]['id']

    return ''

def getLastCrashPoint():
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        return float(objeto_json['records'][0]['crash_point'])

    return 0


def getStatusWinOrLose(autoStop):

    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        if float(objeto_json['records'][0]['crash_point']) >= autoStop:
            return "WIN"

        return "LOSE"

    return "SAME"


def getHistory():

    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        return json.loads(req.text)

    return None