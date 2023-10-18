import sys
import os
import customtkinter as ctk

path = os.path.dirname(os.path.abspath("SearchHistory"))
path2 = os.path.dirname(os.path.abspath("Wallet"))
path3 = os.path.dirname(os.path.abspath("EnterBlaze"))

sys.path.append(path)
sys.path.append(path2)
sys.path.append(path3)

import SearchHistory
import Wallet
import EnterBlaze
import SearchImage
import pyautogui
import CTkMessagebox
import time

def show_info(info):
    # Default messagebox for showing some information
    CTkMessagebox.CTkMessagebox(title="Info", message=info)

class StrategyTwo:

    def __init__(self, moneyStart, waitCrash, autoStop, thread, stopLose, stopWin, strategyScren, logText, progressBarWin, progressBarLose):
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
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzE1NTQ3OTcsImJsb2NrcyI6W10sImlhdCI6MTY5NzYzOTY4OSwiZXhwIjoxNzAyODIzNjg5fQ.Vqt43P7chEJIi-qKanl3rmLU9K4UvLQW1zGG8owPxDw"
        self.wallet = Wallet.Wallet(self.token)
        self.enterBlaze = EnterBlaze.EnterBlaze(self.token,
                                     self.wallet.getCurrencyType(),
                                     autoStop,
                                     self.wallet.getId())

    def hasToEnter(self):
        return SearchHistory.getDecisionToEnter(self.waitCrash, self.autoStop)

    def addOnLogText(self, message):
        self.logText.insert(ctk.END, message + "\n")

    def setStopWinBar(self):
        self.progressBarWin.set((1 * self.moneyWin) / self.stopWin)

    def setStopLoseBar(self):
        self.progressBarLose.set((1 * self.moneyLose) / self.stopLose)

    def duplicateMoneyOrMoneyStart(self):

        status = SearchHistory.getStatusWinOrLose(self.autoStop)

        if status == "LOSE":
            self.moneyLose += self.money
            self.addOnLogText("LOSE de: " + self.wallet.getCurrencySymbol() + str(self.money))
            self.setStopLoseBar()
            return self.money * 2

        elif status == "WIN":
            return self.moneyStart

        return self.moneyStart

    def startStrategy(self):
        self.addOnLogText("START")

        self.lastId = SearchHistory.getLastIdHistory()

        while True:

            if self.thread.stopped():
                break

            time.sleep(0.6)

            lastIdToCompare = SearchHistory.getLastIdHistory()

            if self.lastId != lastIdToCompare:
                if self.hasToEnter():

                    if self.bought:
                        self.money = self.duplicateMoneyOrMoneyStart()

                    if self.moneyWin >= self.stopWin:
                        show_info("Você chegou em seu STOP WIN de: R$" + str(self.stopWin) + " e ganhou: R$" + str(
                            self.moneyWin))
                        self.thread.stop()
                        break
                    elif self.moneyLose >= self.stopLose:
                        show_info("Você chegou em seu STOP LOSE de: R$" + str(self.stopLose) + " e perdeu: R$" + str(
                            self.moneyLose))
                        self.thread.stop()
                        break

                    # Enta apostar até conseguir
                    while True:

                        if self.enterBlaze.enterCrash(self.money):
                            self.addOnLogText("Entrei, com: " + self.wallet.getCurrencySymbol() + str(self.money))
                            self.bought = True
                            break

                        time.sleep(1.5)

                else:
                    if self.bought:
                        self.addOnLogText("WIN de: " + self.wallet.getCurrencySymbol() + str(((self.money * self.autoStop) - self.money)))
                        self.moneyWin = self.moneyWin + ((self.money * self.autoStop) - self.money)
                        self.setStopWinBar()

                    self.addOnLogText("Esperando o proximo CRASH...")

                    self.bought = False
                    self.money = self.moneyStart

                    time.sleep(4)

                self.lastId = lastIdToCompare

        self.strategyScren.destroy()
