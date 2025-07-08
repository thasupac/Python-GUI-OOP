from tkinter import Tk, ttk, messagebox, Label
from config import ConfigProgram

class Machine(ConfigProgram):
    def __init__(self):
        ##เรียกใช้ SQLdatabaseMachine
        self.machineData() ##เรียก connect ตาราง machine

        ##create gui
        self._createGui()
    
    def _createGui(self):
        self.gui = Tk()
        self.gui.title("Machine")
        self.gui.geometry('1000x700')

        self.label = Label(self.gui, text = 'กำลังข้ามมองสร้างไปก่อน...')
        self.label.pack()

        self.gui.mainloop()

# mc = Machine()
# print(mc.programVersion())