import numpy as np
import cv2
import pyautogui
import os

def getLocationImageOnScreen(nameFile):
    imagem = pyautogui.screenshot()
    imagem.save(os.path.dirname(os.path.abspath(__file__)) + '\imagens.detection\captura.png')

    screen = cv2.imread(os.path.dirname(os.path.abspath(__file__)) + "\\imagens.detection\\captura.png")
    imageDetection = cv2.imread(os.path.dirname(os.path.abspath(__file__)) + "\\imagens.detection\\" + nameFile)
    try:
        res = cv2.matchTemplate(screen, imageDetection, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)
        return loc
    except:
        pass

def isImageOnScreen(nameFile):
    imagem = pyautogui.screenshot()
    imagem.save(os.path.dirname(os.path.abspath(__file__)) + '\imagens.detection\captura.png')

    screen = cv2.imread(os.path.dirname(os.path.abspath(__file__)) + "\\imagens.detection\\captura.png")
    imageDetection = cv2.imread(os.path.dirname(os.path.abspath(__file__)) + "\\imagens.detection\\" + nameFile)
    try:
        res = cv2.matchTemplate(screen, imageDetection, cv2.TM_CCOEFF_NORMED)
        return np.any(res > 0.6)
    except:
        pass