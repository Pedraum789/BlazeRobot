import requests
import json
import AccessCredentials

class AccessHotmart:

    def __init__(self):
        self.token = AccessCredentials.getAcessTokenEduzz()
        self.path = 'https://api2.eduzz.com'

    def getSubscriptionByEmail(self, email):

        status = "only_active=true"
        subscriberEmail = "&client_email={client_email}".format(client_email=email)
        url = self.path + "/subscription/get_contract_list?" + status + subscriberEmail
        headers = {'Token': '{token}'.format(token=self.token)}
        req = requests.get(url, headers=headers)

        if req.status_code == 200:
            return json.loads(req.text)

        return ''

    def clientHasSubscriptionActive(self, email):

        objectResult = self.getSubscriptionByEmail(email)

        if objectResult != '' and objectResult['paginator']['totalRows'] > 0:
            return True

        return False
