import requests
import json

def updateVersion(version):
    f = open("version", "w")
    f.write(version)
    f.close()

def getVersion():
    try:
        f = open("version", "r")
    except:
        return 1
    return float(f.read())


def getLastVersion():
    response = requests.get(
        'https://github.com/Pedraum789/BlazeVersions/blob/master/version')

    return float(json.loads(response.text)['payload']['blob']['rawLines'][0])

def hasUpdate():
    if getLastVersion() > getVersion():
        return True

    return False
