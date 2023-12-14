import mysql.connector as a
mydb = a.connect(host = "localhost", user = "abhi",passwd = "1212")
mycursor = mydb.cursor()

mycursor.execute("select * from abhijeet.student")

result = mycursor.fetchone()

for i in result:
    print(i)