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