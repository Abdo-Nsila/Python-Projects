import customtkinter
import tkinter
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
import os


customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green

def etape1() :
    global date
    date = ""
    window = customtkinter.CTk() # creating custom tkinter window
    #* initial window dimension :
    WIDTH = 1000
    HEIGHT = 700

    #* This code makes the window appear in the middle :
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width-WIDTH) / 2)
    y = int((screen_height-HEIGHT) / 2)

    window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
    window.resizable(False,False)
    window.title("Welcome")


    frame = customtkinter.CTkFrame(master=window , corner_radius= 10 , height=650, width=950)
    frame.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
    

    lbl = customtkinter.CTkLabel(master=frame , text="Create your Account" , font=('Centry Gothic',25))
    lbl.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)

    #! -------------------------------------Nom-------------------------------------
    entry_name = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Nom', font=('Centry Gothic',15))
    entry_name.place(relx=0.3,rely=0.25,anchor=tkinter.CENTER)

    #! -------------------------------------Prenom-------------------------------------
    entry_prenom = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Prenom', font=('Centry Gothic',15))
    entry_prenom.place(relx=0.7,rely=0.25,anchor=tkinter.CENTER)


    #! -------------------------------------Date Naissance-------------------------------------
    def call_date() :

        window_date = customtkinter.CTk() # creating custom tkinter window
        #* initial window_date dimension :
        WIDTH = 300
        HEIGHT = 200

        #* This code makes the window appear in the middle :
        screen_width = window_date.winfo_screenwidth()
        screen_height = window_date.winfo_screenheight()
        x = int((screen_width-WIDTH) / 2)
        y = int((screen_height-HEIGHT) / 2)

        window_date.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        window_date.resizable(False,False)
        window_date.title("Date Naissance")

        lbl_date = customtkinter.CTkLabel(master=window_date , text="Selsect your date of birth" , font=('Centry Gothic',25))
        lbl_date.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)

        cal=DateEntry(window_date,selectmode='day',date_pattern='MM-dd-yyyy')
        cal.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

        def send() :
            date = cal.get_date()
            window_date.destroy()
            dateVar.set(date)

        btn_sendDate = customtkinter.CTkButton(window_date,text="Send" , command=send )
        btn_sendDate.place(relx=0.5,rely=0.75,anchor=tkinter.CENTER)

        window_date.mainloop()

    dateVar = tkinter.StringVar()
    dateVar.set(date)
    date_nais = customtkinter.CTkEntry(master=frame,textvariable=dateVar , height=35 , width=200 , font=('Centry Gothic',15))
    date_nais.place(relx=0.28,rely=0.4,anchor=tkinter.CENTER)

    btn_date = customtkinter.CTkButton(frame,text="...", height=35 , width=35 , command=call_date ,font=('Centry Gothic',20))
    btn_date.place(relx=0.41,rely=0.4,anchor=tkinter.CENTER)


    #! -------------------------------------Country-------------------------------------
    combobox_var = customtkinter.StringVar(value="")  # set initial value
    list_country = ['Maroc','Egypt','Canada','Japon']
    combobox = customtkinter.CTkComboBox(master=frame,
                                        values=list_country, font=('Centry Gothic',15),width=250,
                                        variable=combobox_var)
    combobox.place(relx=0.7,rely=0.4,anchor=tkinter.CENTER)


    #! -------------------------------------Ville-------------------------------------
    entry_ville = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Ville', font=('Centry Gothic',15))
    entry_ville.place(relx=0.3,rely=0.55,anchor=tkinter.CENTER)

    #! -------------------------------------Adresse-------------------------------------
    entry_adresse = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Adresse', font=('Centry Gothic',15))
    entry_adresse.place(relx=0.7,rely=0.55,anchor=tkinter.CENTER)

    def info_login() :
        global nom
        nom = entry_name.get()
        global prenom
        prenom = entry_prenom.get()
        global date_naissance
        date_naissance = dateVar.get()
        global country
        country = combobox.get()
        global ville
        ville = entry_ville.get()
        global adresse
        adresse = entry_adresse.get()

        if nom != "" and prenom != "" and date_naissance != "" and country != "" and ville != "" and adresse != "" :
            window.destroy()
            etape2()
        else :
            messagebox.showwarning("Empty Entrys", "You must complete this entrys !")

    btn_login = customtkinter.CTkButton(master=frame , height=40 , width=240 , text='Next' , corner_radius=7 , command=info_login , font=('Arial',20))
    btn_login.place(relx=0.5 , rely=0.75 , anchor=tkinter.CENTER)


    window.mainloop()













def etape2() :
    
    window = customtkinter.CTk() # creating custom tkinter window
    #* initial window dimension :
    WIDTH = 700
    HEIGHT = 700

    #* This code makes the window appear in the middle :
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width-WIDTH) / 2)
    y = int((screen_height-HEIGHT) / 2)

    window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
    window.resizable(False,False)
    window.title("Welcome")


    frame = customtkinter.CTkFrame(master=window , corner_radius= 10 , height=650, width=950)
    frame.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
    

    lbl = customtkinter.CTkLabel(master=frame , text="Create your Account" , font=('Centry Gothic',28))
    lbl.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)

    #! -------------------------------------Username-------------------------------------
    entry_username = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Username', font=('Centry Gothic',15))
    entry_username.place(relx=0.5,rely=0.35,anchor=tkinter.CENTER)

    #! -------------------------------------Gmail-------------------------------------
    entry_email = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Email', font=('Centry Gothic',15))
    entry_email.place(relx=0.5,rely=0.45,anchor=tkinter.CENTER)

    #! -------------------------------------Telephone-------------------------------------
    entry_telephone = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Telephone', font=('Centry Gothic',15))
    entry_telephone.place(relx=0.5,rely=0.55,anchor=tkinter.CENTER)

    #! -------------------------------------Password-------------------------------------
    entry_password = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Password', font=('Centry Gothic',15))
    entry_password.place(relx=0.5,rely=0.65,anchor=tkinter.CENTER)
    #! -------------------------------------Confirm Password-------------------------------------
    entry_cfrmpassword = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Confirm Password', font=('Centry Gothic',15))
    entry_cfrmpassword.place(relx=0.5,rely=0.75,anchor=tkinter.CENTER)


    #! -----------------------------------------------Button Login--------------------------------------------
    btn_login = customtkinter.CTkButton(master=frame , height=50 , width=250 , text='Create Account' , corner_radius=7 , font=('Arial',20) , command=lambda :  stock_info(entry_username.get(),entry_email.get(),entry_telephone.get(),entry_password.get(),entry_cfrmpassword.get()))
    btn_login.place(relx=0.5 , rely=0.9 , anchor=tkinter.CENTER)

    window.mainloop()


def stock_info(username,email,telephone,password,cfrmpassword) :
    if username != "" and email != "" and telephone != "" and password != "" :
        if password != cfrmpassword :
            messagebox.showwarning("Password non valid", "The confirm password is not correct !")
        else :
            try :
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database = 'users',
                )
                mycursor = mydb.cursor()
                
                sql = "INSERT INTO user (nom , prenom , date_naissance , pays , ville , adresse) VALUES (%s , %s , %s , %s , %s , %s)"
                val = (nom,prenom,date_naissance,country,ville,adresse)
                # ! One Insert in User
                mycursor.execute(sql,val)
                print("1 record inserted in User, ID:", mycursor.lastrowid) 
                mydb.commit()

                sql = "INSERT INTO login (gmail , username , telephone , password) VALUES (%s , %s , %s , %s)"
                val = (email , username , telephone , password)
                # ! One Insert in Login
                mycursor.execute(sql,val)
                print("1 record inserted in Login, ID:", mycursor.lastrowid) 
                mydb.commit()
            except :
                messagebox.showerror("ERREUR", "Connection ERREUR the server is stoped !")
    else :
        messagebox.showwarning("Empty Entrys", "You must complete this entrys !")




    


etape1()
