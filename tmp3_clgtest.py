import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="moulesh23",database="temp")
mycursor=mydb.cursor()
x=2;
y="bnm"
mycursor.execute("select * from stud1 where clg='%s'"%y)
for i in mycursor:
	print(i)