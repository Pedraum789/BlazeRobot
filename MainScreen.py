import customtkinter
import os
import sys
sys.path.append(os.path.abspath("Strategies") + "\StrategyOneFiles")
sys.path.append(os.path.abspath("Strategies") + "\StrategyTwoFiles")
import ViewStrategyOne
import ViewStrategyTwo
import pyautogui
import numpy as np
import cv2
import requests

def main():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")

    mainScreen = customtkinter.CTk()

    mainScreen.title("Robo Blaze")
    mainScreen.iconbitmap(os.path.dirname(os.path.abspath("logo.ico")) + "\\icons\\logo.ico")
    mainScreen.geometry("300x230")

    # Tab Nova
    tabview = customtkinter.CTkTabview(mainScreen, width=270, height= 200)
    tabview.pack()
    tabview.add("Blaze Strategies")
    tabview.tab("Blaze Strategies").grid_columnconfigure(0, weight=1)

    customtkinter.CTkButton(tabview.tab("Blaze Strategies"), text="Estratégia 1", command=lambda : ViewStrategyOne.ViewStrategyOne(mainScreen).startScreen()).place(x=10, y=30)

    customtkinter.CTkButton(tabview.tab("Blaze Strategies"), text="Estratégia 2", command=lambda : ViewStrategyTwo.ViewStrategyTwo(mainScreen).startScreen()).place(x=10, y=80)

    mainScreen.mainloop()

if __name__ == "__main__":
    main()