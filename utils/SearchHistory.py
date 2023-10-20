import requests
import json


def verifyToBuy(waitCrash, autoStop):
    qtd = 0
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)
        for i in range(waitCrash):
            crashPoint = float(objeto_json['records'][i]['crash_point'])
            if (crashPoint < autoStop):
                qtd += 1

        return qtd >= waitCrash

    return False


def getStatus(waitCrash, autoStop):
    qtd = 0
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        for i in range(waitCrash):

            crashPoint = float(objeto_json['records'][i + 1]['crash_point'])

            if crashPoint < autoStop:
                qtd += 1

        if float(objeto_json['records'][0]['crash_point']) >= autoStop and qtd >= waitCrash:
            return "WIN"
        elif float(objeto_json['records'][0]['crash_point']) < autoStop and qtd >= waitCrash:
            return "LOSE"
        else:
            return "SAME"

    return "SAME"


def getLastIdHistory():
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        return objeto_json['records'][0]['id']

    return ''


def getStatusWinOrLose(autoStop):

    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        if float(objeto_json['records'][0]['crash_point']) >= autoStop:
            return "WIN"

        return "LOSE"

    return "SAME"


def getDecisionToEnter(waitCrash, autoStop):

    qtd = 0
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        for i in range(waitCrash):

            if float(objeto_json['records'][i]['crash_point']) < autoStop:
                qtd += 1

        if qtd >= waitCrash:
            return True

        return False

    return False