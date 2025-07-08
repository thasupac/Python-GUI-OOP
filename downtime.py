from tkinter import Tk, ttk, messagebox, Label
from config import ConfigProgram

class Downtime(ConfigProgram):
    def __init__(self):
        ##เรียกใช้ SQLdatabaseDowntime
        self.downTime() ##เรียก connect ตาราง downtime

        ##createGui
        self._createGui()
        
    
    def _createGui(self):
        self.gui = Tk()
        self.gui.title("Downtime")
        self.gui.geometry('1000x700')

        self.label = Label(self.gui, text = 'กำลังข้ามมองสร้างไปก่อน...')
        self.label.pack()

        self.gui.mainloop()
        
        