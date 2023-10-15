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


def getStatusById(waitCrash, autoStop, lastId, bought):
    # Para saber se não foi comprado
    if not bought:
        return "SAME"

    qtd = 0
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)

        point = 0

        for i in range(len(objeto_json['records'])):

            if lastId == objeto_json['records'][i]['id']:
                point = i
                break

        if point != 0:
            point = point - 1

        for i in range(point, point + waitCrash):
            crashPoint = float(objeto_json['records'][i + 1]['crash_point'])

            if crashPoint < autoStop:
                qtd += 1

        if float(objeto_json['records'][point]['crash_point']) >= autoStop and qtd >= waitCrash:
            return "WIN"
        elif float(objeto_json['records'][point]['crash_point']) < autoStop and qtd >= waitCrash:
            return "LOSE"
        else:
            return "SAME"

    return "SAME"