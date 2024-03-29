import os
import sys
import customtkinter
import CTkMessagebox

sys.path.append(os.path.abspath("Strategies") + "\StrategyOneFiles")
sys.path.append(os.path.abspath("Strategies") + "\StrategyTwoFiles")
sys.path.append(os.path.abspath("Strategies") + "\StrategyThreeFiles")
sys.path.append(os.path.abspath("credentials"))
sys.path.append(os.path.abspath("Strategies"))
sys.path.append(os.path.dirname(os.path.abspath("AccessTokenBlaze")))
sys.path.append(os.path.dirname(os.path.abspath("TokenFile")))
sys.path.append(os.path.dirname(os.path.abspath("ThreadProgramStop")))

from update import Version, UpdateVersion
import ViewStrategyOne
import ViewStrategyTwo
import ViewStrategyThree
import AccessHotmart
import UserControl
from utils import ThreadProgramStop
from utils.blaze import AccessTokenBlaze, TokenFile
import webbrowser
import pyautogui
import cv2
import numpy
import time

class MainScreen:

    def __init__(self):
        self.mainScreen = None
        self.tabview = None
        self.websiteToBy = 'https://hotmart.com/'
        self.userControl = None
        self.token = None

    def cancelToken(self):
        self.thread.stop()

    def clearToken(self):
        self.token = None
        TokenFile.addTokenToPc("")
        self.hasTokenButtom.deselect()
        self.abbleButtom(self.buttonconfigureToken)

    def configureToken(self):
        self.thread = ThreadProgramStop.ThreadProgramStop(target=self.setTokenBlaze)
        self.thread.start()
        self.switchButtom(self.buttonconfigureToken)
        self.switchButtom(self.buttomCancel)

    def setTokenBlaze(self):
        self.token = AccessTokenBlaze.getAccessTokenBlaze(self.thread)

        if self.token != None:
            TokenFile.addTokenToPc(self.token)
            self.hasTokenButtom.select()
            self.switchButtom(self.buttomCancel)

    def redirectToBuy(self):
        webbrowser.open(self.websiteToBy)

    def onClosing(self):
        if self.userControl is not None:
            try:
                self.userControl.userNotUsing()
            except:
                pass
        self.mainScreen.destroy()

    def showErrorMessage(self, message):
        CTkMessagebox.CTkMessagebox(title="Error", message=message, icon="cancel")

    def show_checkmark(self, message):
        CTkMessagebox.CTkMessagebox(title="Info", message=message, icon="check", option_1="Ok")

    def validateAccess(self, email):

        if not TokenFile.internetOn():
            self.showErrorMessage("Por favor se conecte na internet.")
            return

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

    def startStrategy(self, number):

        if self.token == None:
            self.showErrorMessage("Não está configurado o Token de acesso.")
            self.hasTokenButtom.deselect()
            return
        else:
            if AccessTokenBlaze.validToken(self.token):
                self.hasTokenButtom.select()
            else:
                self.showErrorMessage("Reconfigure o Token.")
                self.clearToken()
                return

        if number == 1:
            ViewStrategyOne.ViewStrategyOne(self.mainScreen).startScreen()
        elif number == 2:
            ViewStrategyTwo.ViewStrategyTwo(self.mainScreen).startScreen()
        elif number == 3:
            ViewStrategyThree.ViewStrategyThree(self.mainScreen).startScreen()

    def switchButtom(self, buttom):
        if buttom._state == customtkinter.NORMAL:
            buttom.configure(state=customtkinter.DISABLED)
        else:
            buttom.configure(state=customtkinter.NORMAL)

    def abbleButtom(self, buttom):
        buttom.configure(state=customtkinter.NORMAL)

    # Tab Estratégias
    def createTabStrategies(self):

        #Caso ja exista o token
        self.token = TokenFile.getTokenOnPc()

        self.mainScreen.geometry("550x220")

        self.tabview.add("Blaze Strategies")
        self.tabview.tab("Blaze Strategies").grid_columnconfigure(0, weight=1)

        customtkinter.CTkButton(self.tabview.tab("Blaze Strategies"), text="Estratégia 1",
                                command=lambda: self.startStrategy(1)).pack(padx=10, pady=10)

        customtkinter.CTkButton(self.tabview.tab("Blaze Strategies"), text="Estratégia 2",
                                command=lambda: self.startStrategy(2)).pack(padx=10, pady=10)

        customtkinter.CTkButton(self.tabview.tab("Blaze Strategies"), text="Estratégia 3",
                                command=lambda: self.startStrategy(3)).pack(padx=10, pady=10)

        # Deleta a Tab login
        self.tabview.delete("Login")

        # Create config Frame
        self.configFrame = customtkinter.CTkFrame(self.mainScreen)
        self.configFrame.grid(row=0, column=0, padx=(10, 10), pady=(24, 10), sticky="nsew")

        self.buttonconfigureToken = customtkinter.CTkButton(self.configFrame, text="Configurar Token",
                                                   command= self.configureToken)
        self.buttonconfigureToken.grid(row=0, column=0, padx=(50, 50), pady=(10, 10), sticky="nsew")

        self.hasTokenButtom = customtkinter.CTkCheckBox(master=self.configFrame, text="Configurado")
        self.hasTokenButtom.grid(row=1, column=0, pady=10, padx=10, sticky="n")
        self.hasTokenButtom.configure(state="disabled")

        if self.token != None and AccessTokenBlaze.validToken(self.token):
            self.hasTokenButtom.select()
            self.switchButtom(self.buttonconfigureToken)
        else:
            self.hasTokenButtom.deselect()

        self.buttomCancel = customtkinter.CTkButton(self.configFrame, text="Cancelar", command= self.cancelToken, state=customtkinter.DISABLED)
        self.buttomCancel.grid(row=2, column=0, padx=(50, 50), pady=(10, 10), sticky="nsew")

        self.buttomClearToken = customtkinter.CTkButton(self.configFrame, text="Limpar Token", command=self.clearToken)
        self.buttomClearToken.grid(row=3, column=0, padx=(50, 50), pady=(10, 10), sticky="nsew")

    def update(self):
        if not TokenFile.internetOn():
            self.showErrorMessage("Por favor se conecte na internet.")
            return

        if Version.hasUpdate():
            UpdateVersion.UpdateVersion(self.mainScreen).updateVersion()
        else:
            self.show_checkmark("Seu app já está atualizado")

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

        customtkinter.CTkButton(self.tabview.tab("Login"), text="Update", command=self.update).pack(
            padx=7, pady=7)

    def main(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.mainScreen = customtkinter.CTk()

        self.mainScreen.title("Robo Blaze")
        self.mainScreen.iconbitmap(os.path.dirname(os.path.abspath("logo.ico")) + "\\icons\\logo.ico")
        self.mainScreen.geometry("300x250")
        self.mainScreen.protocol("WM_DELETE_WINDOW", self.onClosing)

        self.mainScreen.grid_rowconfigure(0, weight=1)
        self.mainScreen.grid_columnconfigure((0, 1), weight=1)

        self.tabview = customtkinter.CTkTabview(self.mainScreen, width=270, height=200)
        self.tabview.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.createTabLogin()

        self.mainScreen.mainloop()


if __name__ == "__main__":
    MainScreen().main()
