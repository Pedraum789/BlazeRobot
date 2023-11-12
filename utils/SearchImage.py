_B='\\imagens.detection\\'
_A='\\imagens.detection\\captura.png'
import numpy as np
import cv2
import pyautogui
import os

PATH = os.path.dirname(os.path.abspath("SmartBlaster.exe"))

def getLocationImageOnScreen(nameFile):
	A=pyautogui.screenshot();A.save(PATH+_A);B=cv2.imread(PATH+_A);C=cv2.imread(PATH+_B+nameFile)
	try:D=cv2.matchTemplate(B,C,cv2.TM_CCOEFF_NORMED);E=np.where(D>=.8);return E
	except:pass
def isImageOnScreen(nameFile):
	A=pyautogui.screenshot();A.save(PATH+_A);B=cv2.imread(PATH+_A);C=cv2.imread(PATH+_B+nameFile)
	try:D=cv2.matchTemplate(B,C,cv2.TM_CCOEFF_NORMED);return np.any(D>.6)
	except:pass

def isImageOnScreenFast(nameFile):
	return pyautogui.locateCenterOnScreen(PATH+_B+nameFile,confidence=0.8) != None