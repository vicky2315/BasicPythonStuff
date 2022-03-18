# from num2words import num2words
# f = open("filetrial.txt", "r+")
# for j in f:
#     st = j
# words = num2words(st)
# print(words)
# f.write(" " + words)
# f.close()

import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost"
    user = "root"
    password = "qwerty123"
)

mycursor1 = mydb.cursor()
mycursor1.execute("create table customers (name varchar(255), address varchar(255))")
mycursor1.execute("insert into customers values ('vignesh', 'jakkur'"))

mycursor = mydb.cursor()
mycursor.execute("select * from table1")

myresult = mycursor.fetchall()

for x in myresult
    print(x)