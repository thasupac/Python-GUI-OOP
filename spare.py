from tkinter import Tk, ttk, messagebox, Label
from config import ConfigProgram

class Spare(ConfigProgram):
    def __init__(self):
        ##เรียกใช้ SQLdatabaseSpare
        self.spare() ##เรียก connect ตาราง spare

        ##createGui
        self._createGui()

    def _createGui(self):
        self.gui = Tk()
        self.gui.title("Spare")
        self.gui.geometry('1000x700')

        self.label = Label(self.gui, text = 'กำลังข้ามมองสร้างไปก่อน...')
        self.label.pack()

        self.gui.mainloop()