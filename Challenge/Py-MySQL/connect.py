import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")
[print(i) for i in mycursor]



# sql = "INSERT INTO stagiaire (nom , prenom , id_groupe) VALUES (%s , %s , %s)"

#! One Insert
# val = ("Nsila", "Abdellah" , 10)
# mycursor.execute(sql, val)
# print("1 record inserted, ID:", mycursor.lastrowid) 
# mydb.commit()


#! Multiple Insert
# val = [("Nsila", "Abdellah"),
#       ("Toug","Bachar"),
#         ("Toug","Fouad"),
#        ("Nsila","Youssef"),
#        ("Nsila","Youness"),
#        ("Nsila","Yassine")
#        ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


#! Select all
# mycursor.execute("SELECT * FROM stagiaire")
# sql = "SELECT * FROM stagiaire WHERE nom = 'Nsila' AND prenom = 'Yassine' "
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)


#! Select by order
# sql = "SELECT * FROM stagiaire ORDER BY nom "
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


#! Update column
# sql = "UPDATE stagiaire SET nom = 'Amine' , prenom = 'Nsila' , id_groupe = 7 WHERE id = 1 "
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


#! Delete column
# sql = "DELETE FROM stagiaire WHERE prenom = 'Bachar'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


#! Drop Table
# sql = "DROP TABLE groupe"
# mycursor.execute(sql) 