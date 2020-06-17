import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="moulesh23",database="test_db")
mycursor=mydb.cursor()
x=1;
mycursor.execute("select * from test where Access_No=1");
for i in mycursor:
	print(i)