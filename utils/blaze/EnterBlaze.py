import requests
import json

class EnterBlaze:

    def __init__(self, token, type, autoCashoutAt, walletId):
        self.token = token
        self.path = 'https://blaze-4.com/api'
        self.crashPath = '/crash/round/enter'
        self.type = type
        self.autoCashoutAt = autoCashoutAt
        self.walletId = walletId

    def enterCrash(self, amount):
        headers = {'content-type': 'application/json;charset=UTF-8', 'authorization': 'Bearer {token}'.format(token=self.token)}
        req = requests.post(
            self.path + self.crashPath,
            headers=headers,
            json={
                'amount': amount,
                'type': '"' + self.type + '"',
                'auto_cashout_at': self.autoCashoutAt,
                'wallet_id': self.walletId})

        if req.status_code == 200:
            return True

        return False
