import pyodbc
import configparser
from tkinter import messagebox
class ConfigProgram:
    ##class variable
    config = configparser.ConfigParser()
    config.read('D:/T_thasupac/052_OOP_Python/Python-GUI-OOP-main/OOP GUI/config.ini')

    # def __init__(self, server, database, username, password):
    def __init__(self):
        __host = self.config['Database']['host']
        __port = self.config['Database']['port']
        __user = self.config['Database']['user']
        __password = self.config['Database']['password']

        ##connect to server
        self.statusSQL = self.__connectSQL(__host, __port, __user, __password)

    def __connectSQL(self, __host, __port, __user, __password):

        try:
            # ตัวอย่างโค้ดที่อาจเกิดข้อผิดพลาด
            self.conn = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};'
                f'SERVER={__host};'
                f'DATABASE={__port};'
                f'UID={__user};'
                f'PWD={__password};'
                f'TrustServerCertificate=yes;')
            self.c = self.conn.cursor()
            return True

        except Exception as e:
            messagebox.showinfo('SQL error', '{}'.format(e))
            return False

        
    
    def programVersion(self):
        self.programname = ConfigProgram.config['General']['app_name']
        self.version = ConfigProgram.config['General']['version']

        return [self.programname, self.version]
    
    ##SQL Table Machine
    def machineData(self):
        print("connect SQL Machine")

    ##SQL Table Downtime
    def downTime(self):
        print("connect SQL Downtime")
        
    ##SQL Table Spare
    def spare(self):
        print("connect SQL Spare")
    
    ##SQL Table Tool
    def tool(self):
        print("connect SQL Tools")

# config = ConfigProgram()
# print(config.statusSQL)