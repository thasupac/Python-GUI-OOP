from tkinter import Tk, ttk, messagebox, Label
class Machine:
    def __init__(self):
        self._createGui()
        
    
    def _createGui(self):
        self.gui = Tk()
        self.gui.title("Machine")
        self.gui.geometry('1000x700')

        self.label = Label(self.gui, text = 'กำลังข้ามมองสร้างไปก่อน...')
        self.label.pack()

        self.gui.mainloop()

