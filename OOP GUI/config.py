import pyodbc
class ConnectDatabase:
    def __init__(self, server, database, username, password):
        self.conn = pyodbc.connect(
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
            f'TrustServerCertificate=yes;')
        self.c = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.c.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='mt_workorder' AND xtype='U')
            CREATE TABLE mt_workorder (
                ID INT IDENTITY(1,1) PRIMARY KEY,
                tsid NVARCHAR(100),
                name NVARCHAR(100),
                department NVARCHAR(100),
                machine NVARCHAR(100),
                problem NVARCHAR(500),
                number NVARCHAR(100),
                tel NVARCHAR(100),
                status NVARCHAR(50))""")
        self.conn.commit()

    def insert_mtworkorder(self, tsid, name, department, machine, problem, number, tel):
        with self.conn:
            command = '''
                INSERT INTO mt_workorder (tsid, name, department, machine, problem, number, tel, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            '''
            self.c.execute(command, (tsid, name, department, machine, problem, number, tel, 'new'))

    def view_mtworkorder(self):
        with self.conn:
            self.c.execute("SELECT * FROM mt_workorder")
            return self.c.fetchall()

    def update_mtworkorder(self, tsid, field, newvalue):
        with self.conn:
            command = f"UPDATE mt_workorder SET {field} = ? WHERE tsid = ?"
            self.c.execute(command, (newvalue, tsid))

    def delete_mtworkorder(self, tsid):
        with self.conn:
            self.c.execute("DELETE FROM mt_workorder WHERE tsid = ?", (tsid,))

    def search_mtworkorder(self, keyword):
        with self.conn:
            text_search = f"%{keyword}%"
            command = '''
                SELECT * FROM mt_workorder
                WHERE tsid = ? OR name LIKE ? OR problem LIKE ? OR machine LIKE ?
            '''
            self.c.execute(command, (keyword, text_search, text_search, text_search))
            return self.c.fetchall()

    def close(self):
        self.c.close()
        self.conn.close()
        