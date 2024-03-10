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







# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showerror


# class TemperatureConverter:
#     @staticmethod
#     def fahrenheit_to_celsius(f):
#         return (f - 32) * 5 / 9


# class ConverterFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         # field options
#         options = {'padx': 5, 'pady': 5}

#         # temperature label
#         self.temperature_label = ttk.Label(self, text='Fahrenheit')
#         self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)

#         # temperature entry
#         self.temperature = tk.StringVar()
#         self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
#         self.temperature_entry.grid(column=1, row=0, **options)
#         self.temperature_entry.focus()

#         self.convert_button = ttk.Button(self, text='Convert')
#         self.convert_button['command'] = self.convert
#         self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

#         # result label
#         self.result_label = ttk.Label(self)
#         self.result_label.grid(row=1, columnspan=3, **options)

#         # add padding to the frame and show it
#         self.grid(padx=10, pady=10, sticky=tk.NSEW)

#     def convert(self):
#         """  Handle button click event
#         """
#         try:
#             f = float(self.temperature.get())
#             c = TemperatureConverter.fahrenheit_to_celsius(f)
#             result = f'{f} Fahrenheit = {c:.2f} Celsius'
#             self.result_label.config(text=result)
#         except ValueError as error:
#             showerror(title='Error', message=error)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title('Temperature Converter')
#         self.geometry('300x70')
#         self.resizable(False, False)


# if __name__ == "__main__":
#     app = App()
#     ConverterFrame(app)
#     app.mainloop()