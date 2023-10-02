import requests
import json

def verifyToBuy(waitCrash, autoStop):
    qtd = 0
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)
        for i in range(waitCrash):
            crashPoint = float(objeto_json['records'][i]['crash_point'])
            if(crashPoint <= autoStop):
               qtd += 1
               
        return qtd >= waitCrash
        
    return False

def getStatus(waitCrash, autoStop):
    qtd = 0
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)
        
        for i in range(len(objeto_json['records'])):
            
            crashPoint = float(objeto_json['records'][i]['crash_point'])
            
            # Perdeu
            if(crashPoint <= autoStop):
                break
            
            qtd += 1

        if(qtd > waitCrash):
            return "WIN"
        elif(qtd == waitCrash):
            return "SAME"
        else:
            return "LOSE"
        
    return "LOSE"

def getLastIdHistory():
    req = requests.get('https://blaze-1.com/api/crash_games/history')

    if req.status_code == 200:
        objeto_json = json.loads(req.text)
        
        return objeto_json['records'][0]['id']
    
    return ''