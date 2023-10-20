from urllib import request
import datetime
import sys
import os

PATH = os.path.dirname(os.path.abspath("SmartBlaster.py"))

def addTokenToPc(token):
    f = open(PATH + "\\token.txt", "w")
    f.write(token)
    f.close()

def getTokenOnPc():
    try:
        f = open(PATH + "\\token.txt", "r")
    except:
        return None
    return f.read()


def internetOn():
    try:
        request.urlopen('http://google.com', timeout=1)
        return True
    except request.URLError as err:
        return False

def addLogHistory(log):
    f = open(PATH + "\\log_history.txt", "a")
    f.write(str(datetime.datetime.now()) + " -> " + log + "\n")
    f.close()