from urllib import request
import datetime

def addTokenToPc(token):
    f = open("token.txt", "w")
    f.write(token)
    f.close()

def getTokenOnPc():
    try:
        f = open("token.txt", "r")
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
    f = open("log_history.txt", "a")
    f.write(str(datetime.datetime.now()) + " -> " + log + "\n")
    f.close()