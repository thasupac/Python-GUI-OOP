from tkinter import Tk, ttk, messagebox, Label
class Tool:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Tool")
        self.gui.geometry('1000x700')

        self.label = Label(self.gui, text = 'กำลังข้ามมองสร้างไปก่อน...')
        self.label.pack()

        self.gui.mainloop()