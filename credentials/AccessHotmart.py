import requests
import json
import AccessCredentials

class AccessHotmart:

    def __init__(self):
        self.bearerToken = AccessCredentials.getAcessToken()
        self.path = 'https://sandbox.hotmart.com'

    def getSaleHistoryByEmail(self, email):

        transactionStatus = "transaction_status={transaction_status}".format(transaction_status="APPROVED")
        buyerEmail = "&buyer_email={buyer_email}".format(buyer_email=email)
        url = self.path + "/payments/api/v1/sales/history?" + transactionStatus + buyerEmail
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {bearer_token}'.format(bearer_token=self.bearerToken)}
        req = requests.get(url, headers=headers)

        if req.status_code == 200:
            return json.loads(req.text)

        return ''

    def getSubscriptionByEmail(self, email):

        status = "status={status}".format(status="ACTIVE")
        subscriberEmail = "&subscriber_email={subscriber_email}".format(subscriber_email=email)
        url = self.path + "/payments/api/v1/subscriptions?" + status + subscriberEmail
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {bearer_token}'.format(bearer_token=self.bearerToken)}
        req = requests.get(url, headers=headers)

        if req.status_code == 200:
            return json.loads(req.text)

        return ''

    def clientHasSubscriptionActive(self, email):

        objectResult = self.getSubscriptionByEmail(email)

        if objectResult != '' and objectResult['page_info']['total_results'] > 0:
            return True

        return False

    def clientHasPayed(self, email):

        objectResult = self.getSaleHistoryByEmail(email)

        if (objectResult != '' and objectResult['page_info']['total_results'] > 0):
            return True

        return False