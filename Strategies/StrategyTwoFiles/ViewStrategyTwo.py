import customtkinter as ctk
import StrategyTwo
from ThreadProgramStop import ThreadProgramStop
import os
from sys import platform

class ViewStrategyTwo: 
    
    def __init__(self, screen):
        self.thread = None
        self.screen = screen
        self.buttonStart = None
        self.buttonExit = None
        self.textResult = None
    
    def changeAlert(self, text):
        self.textResult.configure(text = str(text))
        
    def validMoneyStart(self, moneyStart):
        
        try:
            value = float(moneyStart.get())
            
            if(value <= 0.1):
                self.changeAlert("Valor deve ser >= 0.1")
                return True
        except: 
            if("," in moneyStart.get()):
                self.changeAlert("Valor deve ser com '.' ao invés de ','.")
                return True
            
            self.changeAlert("Valor deve ser um número.")
            return True
        
        return False
    
    def validWaitCrash(self, waitCrash):
        if(not str.isdigit(waitCrash.get()) or int(waitCrash.get()) <= 0):
            self.changeAlert("Valor de crash deve ser número > 0.")
            return True
        
        return False
    
    def validAutoStop(self, autoStop):
        try:
            value = int(autoStop.get())
            
            if(value <= 1):
                self.changeAlert("Valor de auto-stop deve ser maior que 1")
                return True
            
        except:             
            self.changeAlert("Valor deve ser um número.")
            return True
        
    def validateToStart(self, moneyStart, waitCrash, autoStop):
        
        if(moneyStart.get() == '' or waitCrash.get() == '' or autoStop.get() == ''):
            self.changeAlert("Todos os campos devem ser preenchidos.")
            return
        
        if(self.validMoneyStart(moneyStart) or self.validWaitCrash(waitCrash) or self.validAutoStop(autoStop)):
            return
            
        self.thread = ThreadProgramStop(target=self.toStart, args=[float(moneyStart.get()), int(waitCrash.get()), int(autoStop.get())])
        self.thread.start()
        
    
    def toStart(self, moneyStart, waitCrash, autoStop):
        self.changeAlert("Executando...")
        self.switchStartButton()
        self.switchExitButton()
        StrategyTwo.StrategyTwo(moneyStart, waitCrash, autoStop, self.thread).startStrategy()
    
    def switchStartButton(self):
        if (self.buttonStart._state == ctk.NORMAL):
            self.buttonStart.configure(state=ctk.DISABLED)
        else:
            self.buttonStart.configure(state=ctk.NORMAL)
    
    def switchExitButton(self):
        if (self.buttonExit._state == ctk.NORMAL):
            self.buttonExit.configure(state=ctk.DISABLED)
        else:
            self.buttonExit.configure(state=ctk.NORMAL)
        
    def exit(self, screenTopLevel):
        self.thread.stop()
        screenTopLevel.destroy()
        screenTopLevel.update()
    
    def startScreen(self):
        strategyScren = ctk.CTkToplevel(self.screen)
        strategyScren.title("Estratégia 2")
        strategyScren.geometry("1030x350")
        strategyScren.iconbitmap(os.path.dirname(os.path.abspath("logo.ico")) + "\\icons\\logo.ico")
        
        if platform.startswith("win"):
            strategyScren.after(200, lambda: strategyScren.iconbitmap(os.path.dirname(os.path.abspath("logo.ico")) + "\\icons\\logo.ico"))
        
        ctk.CTkLabel(strategyScren, text="Na estratégia 2 você deve configurar o valor da aposta, quantos CRASHES deve esperar até que apostar e o valor que configurou na blaze de auto-retirar.").pack()
        ctk.CTkLabel(strategyScren, text="O robô irá apostar APENAS após a quantidade de crash do valor de auto-stop. Após apostar, caso perca, ele irá duplicar o valor inicial").pack()
        ctk.CTkLabel(strategyScren, text="Exemplo: Seu auto-stop é de 2x, e você colocou para esperar 5 crashes, o sistema vai esperar crashar 5x o valor menor que 2x, para apostar. Caso perca, ele irá duplicar o valor.").pack()
        
        moneyStart = ctk.CTkEntry(strategyScren, placeholder_text= "Valor de aposta R$", width=125)
        moneyStart.pack(padx=5, pady=5)
        
        waitCrash = ctk.CTkEntry(strategyScren, placeholder_text= "Esperar 'x' CRASHED até apostar", width=200)
        waitCrash.pack(padx=5, pady=5)
        
        autoStop = ctk.CTkEntry(strategyScren, placeholder_text= "Valor de auto-stop", width=125)
        autoStop.pack(padx=5, pady=5)
        
        self.buttonStart = ctk.CTkButton(strategyScren, text="START", command=lambda: self.validateToStart(moneyStart, waitCrash, autoStop))
        self.buttonStart.pack(padx=5, pady=8)
        
        self.buttonExit = ctk.CTkButton(strategyScren, text="QUIT", command=lambda : self.exit(strategyScren), state=ctk.DISABLED)
        self.buttonExit.pack(padx=5, pady=8)
        
        self.textResult = ctk.CTkLabel(strategyScren, text="")
        self.textResult.pack(padx=5, pady=8)
        