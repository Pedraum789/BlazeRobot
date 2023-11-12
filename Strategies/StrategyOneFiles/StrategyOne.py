import sys
import os

sys.path.append(os.path.dirname(os.path.abspath("SearchHistory")))
sys.path.append(os.path.dirname(os.path.abspath("Wallet")))
sys.path.append(os.path.abspath("Strategies"))

from utils import SearchHistory
import Strategy

class StrategyOne(Strategy.Strategy):

    def __init__(self, moneyStart, waitCrash, autoStop, thread, stopLose, stopWin, strategyScren, logText, progressBarWin, progressBarLose):
        super().__init__(moneyStart, waitCrash, autoStop, thread, stopLose, stopWin, strategyScren, logText, progressBarWin, progressBarLose)

    def duplicateMoneyOrMoneyStart(self):

        status = SearchHistory.getStatusWinOrLose(self.autoStop)

        if status == "LOSE":
            self.moneyLose += self.money
            self.moneyWin = self.moneyWin - self.money
            self.addOnLogText("LOSE de: " + self.wallet.getCurrencySymbol() + str(self.money))
            self.setStopLoseBar()
            return self.moneyStart

        elif status == "WIN":
            self.setStopWinBar()
            return self.moneyStart

        return self.moneyStart

    def isToDuplicatedMoney(self):
        return self.bought

    def hasToEnter(self):
        qtd = 0

        json = SearchHistory.getHistory()

        if json is not None:

            for i in range(self.waitCrash):

                if float(json['records'][i]['crash_point']) < self.autoStop:
                    qtd += 1

            if qtd >= self.waitCrash:
                return True

            return False

        return False

    def printStart(self):
        self.addOnLogText("-----------------------")
        self.addOnLogText("Iniciado - Estratégia 1")