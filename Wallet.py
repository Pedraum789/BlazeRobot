import requests
import json

class Wallet:

    def __init__(self, token):
        self.token = token
        self.path = 'https://blaze-4.com/api/wallets'
        self.id = None
        self.balance = None
        self.currency_type = None
        self.currency_symbol = None
        self.getWallet()

    def getWallet(self):
        headers = {'authorization': 'Bearer {token}'.format(token=self.token)}
        req = requests.get(self.path, headers=headers)

        if req.status_code == 200:
            jsonWallet = json.loads(req.text)[0]
            self.id = int(jsonWallet['id'])
            self.balance = float(jsonWallet['balance'])
            self.currency_type = str(jsonWallet['currency_type'])
            self.currency_symbol = str(jsonWallet['currency']['symbol'])

    def updateWallet(self):
        headers = {'authorization': 'Bearer {token}'.format(token=self.token)}
        req = requests.get(self.path, headers=headers)

        if req.status_code == 200:
            jsonWallet = json.loads(req.text)[0]
            self.id = int(jsonWallet['id'])
            self.balance = float(jsonWallet['balance'])
            self.currency_type = str(jsonWallet['currency_type'])

    def getId(self):
        return self.id

    def getCurrencySymbol(self):
        return self.currency_symbol

    def getCurrencyType(self):
        return self.currency_type