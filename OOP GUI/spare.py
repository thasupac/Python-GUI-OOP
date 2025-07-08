from tkinter import Tk, ttk, messagebox, Label
class Spare:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Spare")
        self.gui.geometry('1000x700')

        self.label = Label(self.gui, text = 'กำลังข้ามมองสร้างไปก่อน...')
        self.label.pack()

        self.gui.mainloop()