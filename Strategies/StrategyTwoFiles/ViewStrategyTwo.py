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
        self.logText = None
    
    def changeAlert(self, text):
        self.textResult.configure(text = str(text))

    def validFloatValue(self, floatValue, field):

        try:
            value = float(floatValue.get())

            if value < 0.1:
                self.changeAlert("Valor de " + field + " deve ser >= 0.1")
                return True
        except:
            if "," in floatValue.get():
                self.changeAlert("Valor de " + field + " deve ser com '.' ao invés de ','.")
                return True

            self.changeAlert("Valor de " + field + " deve ser um número.")
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
        
    def validateToStart(self, moneyStart, waitCrash, autoStop, stopLose, stopWin, strategyScren):
        
        if(moneyStart.get() == '' or waitCrash.get() == '' or autoStop.get() == '' or stopLose.get() == '' or stopWin.get() == ''):
            self.changeAlert("Todos os campos devem ser preenchidos.")
            return

        if (self.validFloatValue(moneyStart, "aposta") or
                self.validWaitCrash(waitCrash) or
                self.validAutoStop(autoStop) or
                self.validFloatValue(stopLose, "STOP LOSE") or
                self.validFloatValue(stopWin, "STOP WIN")):
            return
            
        self.thread = ThreadProgramStop(target=self.toStart, args=[float(moneyStart.get()), int(waitCrash.get()), int(autoStop.get()), float(stopLose.get()), float(stopWin.get()), strategyScren])
        self.thread.start()
        
    
    def toStart(self, moneyStart, waitCrash, autoStop, stopLose, stopWin, strategyScren):
        self.changeAlert("")
        self.progressbarStart.grid(row=10, column=0, columnspan=3, padx=(10, 10), pady=(5, 5), sticky="ew")
        self.progressbarStart.start()
        self.switchStartButton()
        self.switchExitButton()
        StrategyTwo.StrategyTwo(moneyStart, waitCrash, autoStop, self.thread, stopLose, stopWin, strategyScren, self.logText, self.progressbarStart, self.progressBarLose).startStrategy()
    
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
        strategyScren.geometry("600x450")
        strategyScren.minsize(800, 450)
        strategyScren.iconbitmap(os.path.dirname(os.path.abspath("logo.ico")) + "\\icons\\logo.ico")

        # create 8x2 grid system
        strategyScren.grid_rowconfigure(10, weight=1)
        strategyScren.grid_columnconfigure((0, 1, 2), weight=1)
        
        if platform.startswith("win"):
            strategyScren.after(200, lambda: strategyScren.iconbitmap(os.path.dirname(os.path.abspath("logo.ico")) + "\\icons\\logo.ico"))

        # create textbox
        textbox = ctk.CTkTextbox(strategyScren, width=200)
        textbox.grid(row=0, column=0, rowspan=6, padx=(20, 0), pady=(20, 0), sticky="nsew")
        textbox.insert("0.0",
                       "Explicação\n\n" +
                       "Na estratégia 2 você deve configurar o valor da aposta, quantos CRASHES deve esperar até que apostar e o valor que configurou na blaze de auto-retirar.\n\n" +
                       "O robô irá apostar APENAS após a quantidade de crash do valor de auto-stop. Após apostar, caso perca, ele irá duplicar o valor inicial\n\n" +
                       "Exemplo: Seu auto-stop é de 2x, e você colocou para esperar 5 crashes, o sistema vai esperar crashar 5x o valor menor que 2x, para apostar. Caso perca, ele irá duplicar o valor.\n\n")

        ctk.CTkLabel(strategyScren, text="Valor de aposta").grid(row=0, column=1)
        moneyStart = ctk.CTkEntry(strategyScren, placeholder_text= "R$", width=125)
        moneyStart.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        ctk.CTkLabel(strategyScren, text="Quantidade de CRASH").grid(row=2, column=1)
        waitCrash = ctk.CTkEntry(strategyScren, width=200)
        waitCrash.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        ctk.CTkLabel(strategyScren, text="Valor informado de auto-stop").grid(row=4, column=1)
        autoStop = ctk.CTkEntry(strategyScren, width=125)
        autoStop.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        ctk.CTkLabel(strategyScren, text="Stop LOSE").grid(row=6, column=0)
        stopLose = ctk.CTkEntry(strategyScren, width=30)
        stopLose.grid(row=7, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.progressBarLose = ctk.CTkProgressBar(strategyScren, mode='determinate')
        self.progressBarLose.set(0)
        self.progressBarLose.grid(row=8, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

        ctk.CTkLabel(strategyScren, text="Stop WIN").grid(row=6, column=1)
        stopWin = ctk.CTkEntry(strategyScren, width=30)
        stopWin.grid(row=7, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")
        self.progressBarWin = ctk.CTkProgressBar(strategyScren, mode='determinate')
        self.progressBarWin.set(0)
        self.progressBarWin.grid(row=8, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

        self.buttonExit = ctk.CTkButton(strategyScren, text="QUIT", command=lambda : self.exit(strategyScren), state=ctk.DISABLED)
        self.buttonExit.grid(row=9, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.buttonStart = ctk.CTkButton(strategyScren, text="START", command=lambda: self.validateToStart(moneyStart, waitCrash, autoStop, stopLose, stopWin, strategyScren))
        self.buttonStart.grid(row=9, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.textResult = ctk.CTkLabel(strategyScren, text="")
        self.textResult.grid(row=10, column=0, columnspan=2, padx=(10, 10), pady=(5, 5), sticky="nsew")

        self.progressbarStart = ctk.CTkProgressBar(strategyScren)
        self.progressbarStart.configure(mode="indeterminnate")

        self.logText = ctk.CTkTextbox(strategyScren, width=230)
        self.logText.grid(row=0, column=3, rowspan=10, padx=(10, 10), pady=(10, 10), sticky="nsew")
        