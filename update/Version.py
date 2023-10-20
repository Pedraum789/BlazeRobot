import requests
import json
import sys
import os

PATH = os.path.dirname(os.path.abspath("SmartBlaster.py"))

def updateVersion(version):
    f = open(PATH + "\\version", "w")
    f.write(version)
    f.close()

def getVersion():
    try:
        f = open(PATH + "\\version", "r")
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
