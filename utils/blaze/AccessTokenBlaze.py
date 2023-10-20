import pyautogui
import time
import pyperclip
import sys
import os

sys.path.append(os.path.abspath("utils"))

from utils import SearchImage
import requests

def getAccessTokenBlaze(thread):
    while True:

        if thread.stopped():
            break

        if SearchImage.isImageOnScreenFast("blaze_logo.png"):

            toClick = SearchImage.getLocationImageOnScreen("blaze_logo.png")

            pyautogui.moveTo(toClick[1][0], toClick[0][0])
            pyautogui.click()

            time.sleep(1)

            pyautogui.hotkey('ctrl', 'shift', 'i')
            time.sleep(6)
            pyautogui.hotkey('ctrl', "'")

            key = 'copy(localStorage.ACCESS_TOKEN)'

            for i in range(len(list(str(key)))):
                pyautogui.press(list(str(key))[i])

            pyautogui.press('ENTER')

            return pyperclip.paste()

    return None


def validToken(token):
    req = requests.get("https://blaze-4.com/api/users/me",
                       headers={'authorization': 'Bearer {token}'.format(token=token)})

    if req.status_code == 200:
        return True

    return False
