import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="moulesh23",database="temp")
mycursor=mydb.cursor()
x=input('enter criteria')
mycursor.execute("select * from stud where clg=x")
for i in mycursor:
	print(i)
