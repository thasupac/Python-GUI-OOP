from tkinter import ttk, Tk, messagebox
from machine import Machine
from spare import Spare
from tools import Tool
from downtime import Downtime

class MainProgram:
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Main")
        self.gui.geometry('500x250')

        ##machineBT
        self.machinebt = ttk.Button(self.gui, text='Machine',command=self.machinepage)
        self.machinebt.pack(ipadx=10, ipady=10)

        ##spareBT
        self.sparebt = ttk.Button(self.gui, text='Spare',command=self.sparepage)
        self.sparebt.pack(ipadx=10, ipady=10)

        ##toolBT
        self.toolbt = ttk.Button(self.gui, text='Tool',command=self.toolpage)
        self.toolbt.pack(ipadx=10, ipady=10)

        ##downtimeBT
        self.downtimebt = ttk.Button(self.gui, text='Downtime',command=self.downtimepage)
        self.downtimebt.pack(ipadx=10, ipady=10)

        self.gui.mainloop()
    
    def machinepage(self):
        self.machine = Machine()
        
    def sparepage(self):
        self.spare = Spare()

    def toolpage(self):
        self.tools = Tool()

    def downtimepage(self):
        self.downtimes = Downtime()

main = MainProgram()