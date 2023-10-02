import sys
import os
path = os.path.dirname(os.path.abspath("SearchHistory"))
sys.path.append(path)
import SearchHistory
import SearchImage
import pyautogui

class StrategyTwo:
    
    def __init__(self, moneyStart, waitCrash, autoStop, thread):
        self.lastId = ''
        self.thread = thread
        self.moneyStart = moneyStart
        self.waitCrash = waitCrash
        self.autoStop = autoStop
        self.money = moneyStart
    
    def duplicateMoneyOrStay(self):
        
        status = SearchHistory.getStatus(self.waitCrash, self.autoStop)
        
        if(status == "LOSE"):
            lastIdCrash = SearchHistory.getLastIdHistory()
            if(self.lastId != lastIdCrash):
                self.lastId = lastIdCrash
                return self.money * 2
        elif(status == "SAME"):
            return self.money
        else:
            return self.moneyStart

        return self.money
        

    def startStrategy(self):
        self.lastId = SearchHistory.getLastIdHistory()
        print("COMECEI")
        while True:
            
            if(self.thread.stopped()):
                print("PAREI")
                break
            
            if(SearchImage.isImageOnScreen("crashed_2.png") and not SearchImage.isImageOnScreen("wait_line.png")):
                
                quantity = SearchImage.getLocationImageOnScreen("quantia.png")
                pyautogui.moveTo(quantity[1][0], quantity[0][0])
                pyautogui.click()
                    
                if(SearchHistory.verifyToBuy(self.waitCrash, self.autoStop)):
                    
                    self.money = self.duplicateMoneyOrStay()
                    for key in range(len(list(str(self.money)))):
                        pyautogui.hotkey(list(str(self.money))[key])
                    
                    try:
                        startGame = SearchImage.getLocationImageOnScreen("start_game_3.png")
                        pyautogui.moveTo(startGame[1][0], startGame[0][0])
                        pyautogui.click()
                    except:
                        pass