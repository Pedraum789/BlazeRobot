import sys
import os
path = os.path.dirname(os.path.abspath("SearchHistory"))
sys.path.append(path)
import SearchHistory
import SearchImage
import pyautogui

def startStrategy(moneyStart, waitCrash, autoStop, thread):
    
    print("COMECEI")
    
    while True:
        
        if(thread.stopped()):
            print("PAREI")
            break
        
        if(SearchImage.isImageOnScreen("crashed_2.png") and not SearchImage.isImageOnScreen("wait_line.png")):
            
            quantity = SearchImage.getLocationImageOnScreen("quantia.png")
            pyautogui.moveTo(quantity[1][0], quantity[0][0])
            pyautogui.click()
                
            if(SearchHistory.verifyToBuy(waitCrash, autoStop)):
                
                for key in range(len(list(str(moneyStart)))):
                    pyautogui.hotkey(list(str(moneyStart))[key])
                
                try:
                    startGame = SearchImage.getLocationImageOnScreen("start_game_3.png")
                    pyautogui.moveTo(startGame[1][0], startGame[0][0])
                    pyautogui.click()
                except:
                    pass