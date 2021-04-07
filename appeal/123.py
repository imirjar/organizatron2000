import pyodbc

bsk_number = 36126113496780804
server = '192.168.6.111\sod'
database = 'BaseSOD' 
username = 'sa' 
password = 'SOD-Server' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM baseSOD.dbo.SendPayment WHERE CardNumber = '%s' AND (Status = 0 OR Status = 41 OR Status = 61);"%bsk_number)
#cursor.execute("SELECT * FROM baseSOD.dbo.BlackList;") 
row = cursor.fetchall() 
print(row)
