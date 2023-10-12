import os
import sys

path = os.path.dirname(os.path.abspath("SearchHistory"))
sys.path.append(path)
import SearchHistory
import SearchImage
import pyautogui

def show_info(info):
    # Default messagebox for showing some information
    CTkMessagebox(title="Info", message=info)

class StrategyTwo:

    def __init__(self, moneyStart, waitCrash, autoStop, thread, stopLose, stopWin):
        self.lastId = ''
        self.lastIdToNotRepeat = ''
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

    def duplicateMoneyOrStay(self):

        status = SearchHistory.getStatusById(self.waitCrash, self.autoStop, self.lastId, self.bought)

        if status == "LOSE":
            lastIdCrash = SearchHistory.getLastIdHistory()
            if self.lastIdToNotRepeat != lastIdCrash:
                self.moneyLose += self.money
                print("LAST ID -> " + self.lastId)
                print("LOSE -> " + str(self.moneyLose))
                print("---------------")
                self.lastIdToNotRepeat = lastIdCrash
                return self.money
        elif status == "WIN":
            lastIdCrash = SearchHistory.getLastIdHistory()
            if self.lastIdToNotRepeat != lastIdCrash:
                self.moneyWin = self.moneyWin + ((self.money * self.autoStop) - self.money)
                print("LAST ID -> " + self.lastId)
                print("WIN -> " + str(self.moneyWin))
                print("---------------")
                self.lastIdToNotRepeat = lastIdCrash
                return self.moneyStart
        else:
            print("LAST ID -> " + self.lastId)
            print("SAME")
            print("---------------")
            return self.money

    def startStrategy(self):
        self.lastId = SearchHistory.getLastIdHistory()
        print("COMECEI")
        while True:

            if self.thread.stopped():
                print("PAREI")
                break

            if self.moneyWin >= self.stopWin:
                self.thread.stop()
                show_info("Você chegou em seu STOP WIN de: R$" + str(self.stopWin) + " e ganhou: R$" + str(self.moneyWin))
                break
            elif self.moneyLose >= self.stopLose:
                self.thread.stop()
                show_info("Você chegou em seu STOP LOSE de: R$" + str(self.stopLose) + " e perdeu: R$" + str(self.moneyLose))
                break

            if SearchImage.isImageOnScreen("crashed_2.png") and not SearchImage.isImageOnScreen("wait_line.png"):
                try:
                    quantity = SearchImage.getLocationImageOnScreen("quantia.png")
                    pyautogui.moveTo(quantity[1][0], quantity[0][0])
                    pyautogui.click()

                    self.money = self.duplicateMoneyOrStay()

                    if SearchHistory.verifyToBuy(self.waitCrash, self.autoStop):

                        for key in range(len(list(str(self.money)))):
                            pyautogui.hotkey(list(str(self.money))[key])

                        startGame = SearchImage.getLocationImageOnScreen("start_game_3.png")
                        pyautogui.moveTo(startGame[1][0], startGame[0][0])
                        pyautogui.click()
                        self.bought = True
                        self.lastId = SearchHistory.getLastIdHistory()
                except:
                    pass
