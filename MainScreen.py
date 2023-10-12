import os
import sys
import customtkinter
from CTkMessagebox import CTkMessagebox

sys.path.append(os.path.abspath("Strategies") + "\StrategyOneFiles")
sys.path.append(os.path.abspath("Strategies") + "\StrategyTwoFiles")
sys.path.append(os.path.abspath("credentials"))

import ViewStrategyOne
import ViewStrategyTwo
import AccessHotmart
import UserControl
import webbrowser
import cv2
import requests
import pyautogui
import numpy as np

class MainScreen:

    def __init__(self):
        self.mainScreen = None
        self.tabview = None
        self.websiteToBy = 'https://hotmart.com/'
        self.userControl = None

    def redirectToBuy(self):
        webbrowser.open(self.websiteToBy)

    def onClosing(self):
        if self.userControl is not None:
            self.userControl.userNotUsing()
        self.mainScreen.destroy()

    def showErrorMessage(self, message):
        CTkMessagebox(title="Error", message=message, icon="cancel")

    def validateAccess(self, email):
        self.userControl = UserControl.UserControl(email)

        if AccessHotmart.AccessHotmart().clientHasSubscriptionActive(email):
            if(self.userControl.userUsing()):
                self.createTabStrategies()
            else:
                self.userControl = None
                self.showErrorMessage("Há um usuário utilizando o programa. Entre em contato com o administrador.")
        else:
            self.userControl = None
            self.showErrorMessage("O usuário de email não está cadastrado. Entre em contato com o administrador.")

    # Tab Estratégias
    def createTabStrategies(self):

        self.tabview.add("Blaze Strategies")
        self.tabview.tab("Blaze Strategies").grid_columnconfigure(0, weight=1)

        customtkinter.CTkButton(self.tabview.tab("Blaze Strategies"), text="Estratégia 1",
                                command=lambda: ViewStrategyOne.ViewStrategyOne(self.mainScreen).startScreen()).pack(
            padx=10,
            pady=10)

        customtkinter.CTkButton(self.tabview.tab("Blaze Strategies"), text="Estratégia 2",
                                command=lambda: ViewStrategyTwo.ViewStrategyTwo(self.mainScreen).startScreen()).pack(
            padx=10,
            pady=10)

        # Deleta a Tab login
        self.tabview.delete("Login")

    # Tab Login
    def createTabLogin(self):

        self.tabview.add("Login")
        self.tabview.tab("Login").grid_columnconfigure(0, weight=1)

        email = customtkinter.CTkEntry(self.tabview.tab("Login"), placeholder_text="Email", width=200)
        email.pack(padx=7, pady=7)

        customtkinter.CTkButton(self.tabview.tab("Login"), text="Login",
                                command=lambda: self.validateAccess(email.get())).pack(
            padx=7, pady=7)

        customtkinter.CTkButton(self.tabview.tab("Login"), text="Comprar", command=self.redirectToBuy).pack(padx=7, pady=7)

    def main(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.mainScreen = customtkinter.CTk()

        self.mainScreen.title("Robo Blaze")
        self.mainScreen.iconbitmap(os.path.dirname(os.path.abspath("logo.ico")) + "\\icons\\logo.ico")
        self.mainScreen.geometry("300x230")
        self.mainScreen.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.tabview = customtkinter.CTkTabview(self.mainScreen, width=270, height=200)
        self.tabview.pack()

        self.createTabLogin()

        self.mainScreen.mainloop()


if __name__ == "__main__":
    MainScreen().main()
