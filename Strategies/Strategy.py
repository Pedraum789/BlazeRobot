import sys
import os

path = os.path.dirname(os.path.abspath("SearchHistory"))
path2 = os.path.dirname(os.path.abspath("Wallet"))
path3 = os.path.dirname(os.path.abspath("EnterBlaze"))
path4 = os.path.dirname(os.path.abspath("TokenFile"))

sys.path.append(path)
sys.path.append(path2)
sys.path.append(path3)
sys.path.append(path4)

from abc import ABC, abstractmethod
import CTkMessagebox
import time
from utils import SearchHistory
from utils.blaze import EnterBlaze, Wallet, TokenFile


def show_info(info):
    # Default messagebox for showing some information
    CTkMessagebox.CTkMessagebox(title="Info", message=info)

class Strategy(ABC):

    def __init__(self, moneyStart, waitCrash, autoStop, thread, stopLose, stopWin, strategyScren, logText, progressBarWin, progressBarLose):
        self.status = None
        self.idBought = None
        self.lastId = ''
        self.thread = thread
        self.moneyStart = moneyStart
        self.waitCrash = waitCrash
        self.autoStop = autoStop
        self.money = moneyStart
        self.moneyWin = 0
        self.moneyLose = 0
        self.bought = False
        self.stopLose = stopLose
        self.stopWin = stopWin
        self.strategyScren = strategyScren
        self.logText = logText
        self.progressBarWin = progressBarWin
        self.progressBarLose = progressBarLose
        self.token = str(TokenFile.getTokenOnPc())
        self.wallet = Wallet.Wallet(self.token)
        self.enterBlaze = EnterBlaze.EnterBlaze(self.token,
                                                self.wallet.getCurrencyType(),
                                                autoStop,
                                                self.wallet.getId())

    @abstractmethod
    def hasToEnter(self):
        pass

    def addOnLogText(self, message):
        self.logText.insert("0.0", message + "\n")
        TokenFile.addLogHistory(message)

    def setStopWinBar(self):
        self.progressBarWin.set(self.moneyWin / self.stopWin)

    def setStopLoseBar(self):
        self.progressBarLose.set(self.moneyLose / self.stopLose)

    @abstractmethod
    def duplicateMoneyOrMoneyStart(self):
        pass

    @abstractmethod
    def printStart(self):
        pass

    @abstractmethod
    def isToDuplicatedMoney(self):
        pass

    def startStrategy(self):

        self.printStart()

        self.addOnLogText("Dinheiro INICIAL: " + str(self.wallet.getCurrencyType()) + str(self.wallet.getMoney()))

        self.lastId = SearchHistory.getLastIdHistory()

        while True:

            if self.thread.stopped():
                break

            time.sleep(0.6)

            lastIdToCompare = SearchHistory.getLastIdHistory()

            if self.lastId != lastIdToCompare:

                lastCrashCompare = SearchHistory.getLastCrashPoint()

                if lastCrashCompare >= autoStop:
                    self.status = 1
                else:
                    self.status = 0

                if self.hasToEnter():

                    if self.isToDuplicatedMoney():
                        self.money = self.duplicateMoneyOrMoneyStart()

                    if self.moneyWin >= self.stopWin:
                        self.wallet.updateWallet()
                        log = "Você chegou em seu STOP WIN de: R$" + str(self.stopWin) + " e ganhou: R$" + str(self.moneyWin) + "\n" + "Seu salto atual é de: " + str(self.wallet.getCurrencyType()) + str(self.wallet.getMoney())
                        show_info(log)
                        self.addOnLogText(log)
                        self.thread.stop()
                        break
                    elif self.moneyLose >= self.stopLose:
                        self.wallet.updateWallet()
                        log = "Você chegou em seu STOP LOSE de: R$" + str(self.stopLose) + " e perdeu: R$" + str(self.moneyLose) + "\n" + "Seu salto atual é de: " + str(self.wallet.getCurrencyType()) + str(self.wallet.getMon)
                        show_info(log)
                        self.addOnLogText(log)
                        self.thread.stop()
                        break

                    self.wallet.updateWallet()
                    if self.wallet.getMoney() >= self.money:
                        # Enta apostar até conseguir
                        while True:

                            if self.enterBlaze.enterCrash(self.money):
                                self.addOnLogText("Entrei, com: " + str(self.wallet.getCurrencySymbol()) + str(self.money))
                                self.bought = True
                                self.idBought = lastIdToCompare
                                break

                            time.sleep(1.5)
                    else:
                        info = "Você não pode apostar o valor de: " + str(self.wallet.getCurrencySymbol()) + str(self.money) + "\n" + "Seu saldo é de: " + str(self.wallet.getCurrencySymbol()) + str(self.wallet.getMoney())
                        show_info(info)
                        self.addOnLogText(info)
                        self.thread.stop()
                        break
                else:
                    if self.bought:
                        self.addOnLogText("WIN de: " + self.wallet.getCurrencySymbol() + str(((self.money * self.autoStop) - self.money)))
                        self.moneyWin = self.moneyWin + ((self.money * self.autoStop) - self.money)
                        self.moneyLose = self.moneyLose - ((self.money * self.autoStop) - self.money)
                        self.setStopWinBar()

                    self.addOnLogText("Esperando o proximo CRASH...")

                    self.bought = False
                    self.money = self.moneyStart

                    time.sleep(4)

                self.lastId = lastIdToCompare

        self.strategyScren.destroy()