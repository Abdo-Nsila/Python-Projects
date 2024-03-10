import customtkinter
import tkinter
from tkinter import messagebox
import mysql.connector
import os


customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green


window = customtkinter.CTk() # creating custom tkinter window
#* initial window dimension :
WIDTH = 600
HEIGHT = 600

#* This code makes the window appear in the middle :
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width-WIDTH) / 2)
y = int((screen_height-HEIGHT) / 2)

window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
window.resizable(False,False)
window.title("Welcome")


frame = customtkinter.CTkFrame(master=window , corner_radius= 10 , height=500, width=400)
frame.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
 

lbl = customtkinter.CTkLabel(master=frame , text="Log into your Account" , font=('Centry Gothic',25))
lbl.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)


entry1 = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Username / Telephone')
entry1.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)


entry2 = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Password')
entry2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

def info_login(username,password) :
    if username != "" and password != "" :
        try :
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = 'users',
            )
            mycursor = mydb.cursor()

            try :
                #* Handling Username / Telephone Erreur
                sql1 = f"SELECT id_login FROM login WHERE username = '{username}' "
                mycursor.execute(sql1)
                myresult = mycursor.fetchall()
                for i in myresult :
                    id = int(i[0])
                    print(id)

                sql2 = f"SELECT username FROM login WHERE id_login = {id} "
                mycursor.execute(sql2)
                myresult = mycursor.fetchall()
                for i in myresult :
                    usr = str(i[0])
                    print(usr)

                #* Get password
                sql = f"SELECT password FROM login WHERE id_login = {id} "
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for i in myresult :
                    psw = str(i[0])
                    print(psw)
            except :
                messagebox.showerror("ERREUR", "Username / Telephone is incorrect !")

            try :
                if  password == psw :
                    window.destroy()
                    os.system('info_login.py')
                    quit()
                else :
                    raise "Invalide password !"
            
            except :
                messagebox.showerror("ERREUR", "Password is incorrect !")

        except :
                messagebox.showerror("ERREUR", "Connection ERREUR the server is stoped !")





    else :
        messagebox.showwarning("Empty Entrys", "You must complete this entrys !")


    

btn1 = customtkinter.CTkButton(master=frame , height=40 , width=240 , text='Login' , corner_radius=7 , command=lambda : info_login(entry1.get(),entry2.get()) , font=('Arial',20))
btn1.place(relx=0.5 , rely=0.7 , anchor=tkinter.CENTER)

window.mainloop()

