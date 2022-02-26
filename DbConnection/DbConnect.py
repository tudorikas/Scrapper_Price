import pyodbc
import Logger
#conn = pyodbc.connect('Driver={SQL Server};'
#                      'Server=DESKTOP-P5379JT;'
#                      'Database=Preturi;'
#                      'Trusted_Connection=yes;')
#
#cursor = conn.cursor()
#cursor.execute('SELECT * FROM Preturi')
#cursor.close()
#conn.close()

class DbConnect:
    def __init__(self,my_logger):
        self.my_logger=my_logger
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-P5379JT;'
                              'Database=Preturi;'
                              'Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()


    def InsertPrice(self,object,price,site):
        try:
            self.cursor.execute("SELECT ID FROM Preturi Where Nume='"+object+"'")
            val=0
            for a in self.cursor:
                val=a
            if val==0:
                self.cursor.execute("INSERT INTO Preturi (Nume,Site) VALUES ('" + object + "','" + site + "')")
                self.conn.commit()
                self.cursor.execute("SELECT ID FROM Preturi Where Nume='" + object + "'")
                val = 0
                for a in self.cursor:
                    val = a
            self.cursor.execute("INSERT INTO PreturiSite (Pret,IDProdus) VALUES ("+price+","+str(val[0])+")")
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
        except Exception as ex:
            self.my_logger.error(ex)




#a=DbConnect()
#a.InsertPrice("Aragaz","233","aaa")