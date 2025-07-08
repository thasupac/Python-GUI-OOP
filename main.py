from tkinter import ttk, Tk, messagebox
from machine import Machine
from spare import Spare
from tools import Tool
from downtime import Downtime
from config import ConfigProgram
import time

class MainProgram(ConfigProgram):
    def __init__(self):
        self.gui = Tk()
        self.debug = self.programVersion()
        self.gui.title("{} {}".format(self.debug[0], self.debug[1]))
        self.gui.geometry('500x250')

        ##loginBT
        self.loginbt = ttk.Button(self.gui, text='Login')
        self.loginbt.grid(row=0, column=0, ipadx=10, ipady=10)

        ##machineBT
        self.machinebt = ttk.Button(self.gui, text='Machine',command=self.machinepage)
        self.machinebt.grid(row=0, column=1, ipadx=10, ipady=10)

        ##spareBT
        self.sparebt = ttk.Button(self.gui, text='Spare',command=self.sparepage)
        self.sparebt.grid(row=1, column=1, ipadx=10, ipady=10)

        ##toolBT
        self.toolbt = ttk.Button(self.gui, text='Tool',command=self.toolpage)
        self.toolbt.grid(row=2, column=1, ipadx=10, ipady=10)

        ##downtimeBT
        self.downtimebt = ttk.Button(self.gui, text='Downtime',command=self.downtimepage)
        self.downtimebt.grid(row=3, column=1, ipadx=10, ipady=10)

        
        self.gui.after(100, self.conn)
        self.gui.mainloop()
    
    def conn(self):
        ####connect to server
        print(self.statusSQL)
        super().__init__()

    def machinepage(self):
        self.machine = Machine()
        
    def sparepage(self):
        self.spares = Spare()

    def toolpage(self):
        self.tools = Tool()

    def downtimepage(self):
        self.downtimes = Downtime()

main = MainProgram()
