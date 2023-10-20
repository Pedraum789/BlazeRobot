import customtkinter as ctk
from utils.ThreadProgramStop import ThreadProgramStop
import requests
import win32api

_AppName_ = 'smart_blaster_setup'

class UpdateVersion:

    def __init__(self, screen):
        self.screen = screen

    def cancel(self):
        self.t1.stop()
        self.buttomUpdate.configure(state=ctk.NORMAL)

    def update(self):
        self.t1 = ThreadProgramStop(target=self.updateReal)
        self.t1.start()

    def updateReal(self):
        self.progressbarStart.start()
        self.buttomUpdate.configure(state=ctk.DISABLED)
        self.buttomCancel.configure(state=ctk.NORMAL)
        with requests.get("https://github.com/Pedraum789/BlazeVersions/raw/master/" + _AppName_ + ".exe?raw=true", stream=True) as r:
            r.raise_for_status()
            with open(f'./tmp/{_AppName_}.exe', 'wb') as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)

        self.progressbarStart.stop()
        self.buttomInstall.configure(state=ctk.NORMAL)
        self.buttomUpdate.configure(state=ctk.NORMAL)
        self.buttomCancel.configure(state=ctk.DISABLED)
        self.t1.stop()

    def install(self):
        self.progressbarStart.start()
        win32api.ShellExecute(0, 'open', f'tmp\\{_AppName_}.exe', None, None, 10)
        self.progressbarStart.stop()
        self.updateScreen.destroy()
        self.screen.destroy()

    def updateVersion(self):
        self.updateScreen = ctk.CTkToplevel(self.screen)
        self.updateScreen.title("Update")
        self.updateScreen.geometry("500x150")

        self.updateScreen.grid_rowconfigure(1, weight=1)
        self.updateScreen.grid_columnconfigure(3, weight=1)

        self.progressbarStart = ctk.CTkProgressBar(self.updateScreen)
        self.progressbarStart.configure(mode="indeterminnate")
        self.progressbarStart.grid(row=0, column=0, columnspan=3, padx=(10, 10), pady=(20, 20), sticky="ew")

        self.buttomInstall = ctk.CTkButton(self.updateScreen, text="Instalar", command=self.install, state=ctk.DISABLED)
        self.buttomInstall.grid(row=1, column=2, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.buttomUpdate = ctk.CTkButton(self.updateScreen, text="Baixar atualização", command=self.update)
        self.buttomUpdate.grid(row=1, column=1, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.buttomCancel = ctk.CTkButton(self.updateScreen, text="Cancelar", command=self.cancel, state=ctk.DISABLED)
        self.buttomCancel.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")
