_B='\\imagens.detection\\'
_A='\\imagens.detection\\captura.png'
import numpy as np,cv2,pyautogui,os
def getLocationImageOnScreen(nameFile):
	A=pyautogui.screenshot();A.save(os.path.dirname(os.path.abspath("imagens.detection"))+_A);B=cv2.imread(os.path.dirname(os.path.abspath("imagens.detection"))+_A);C=cv2.imread(os.path.dirname(os.path.abspath("imagens.detection"))+_B+nameFile)
	try:D=cv2.matchTemplate(B,C,cv2.TM_CCOEFF_NORMED);E=np.where(D>=.8);return E
	except:pass
def isImageOnScreen(nameFile):
	A=pyautogui.screenshot();A.save(os.path.dirname(os.path.abspath("imagens.detection"))+_A);B=cv2.imread(os.path.dirname(os.path.abspath("imagens.detection"))+_A);C=cv2.imread(os.path.dirname(os.path.abspath("imagens.detection"))+_B+nameFile)
	try:D=cv2.matchTemplate(B,C,cv2.TM_CCOEFF_NORMED);return np.any(D>.6)
	except:pass

def isImageOnScreenFast(nameFile):
	return pyautogui.locateCenterOnScreen(os.path.dirname(os.path.abspath("imagens.detection"))+_B+nameFile,confidence=0.8) != None