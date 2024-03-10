import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
import os.path
from matplotlib.widgets import Button
from datetime import datetime


WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280

#* Get window and screen info
window_width = WINDOW_WIDTH
window_height = WINDOW_HEIGHT


ctk.set_appearance_mode('systeme') #can set light or dark
ctk.set_default_color_theme("green") #themes: blue, dark-blue or green
class App(ctk.CTk) :

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #* initial window dimension :
        WIDTH = 1280
        HEIGHT = 720

        #* This code makes the window appear in the middle :
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width-WIDTH) / 2)
        y = int((screen_height-HEIGHT) / 2)

        self.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        self.resizable(False,False)
        self.title("Expense Tracker")

        self.lbl_name = ctk.CTkLabel(self,text="Enter your full name :",font=('Arial',30)) 
        self.lbl_name.place(relx=0.25,rely=0.1)
        self.entry_name = ctk.CTkEntry(self,height=40,width=260,font=('Arial',30))
        self.entry_name.place(relx=0.55,rely=0.1)

        self.h1 = ctk.CTkLabel(self,text="Expense Tracker",font=('Arial',30),text_color='#fa0')
        self.h1.place(relx=0.4,rely=0.2)


        frm = ctk.CTkFrame(self)
        frm.place(relx=0.3,rely=0.3)
    

        self.lbl_name = ctk.CTkLabel(frm,text="Food :",font=('Arial',30)) 
        self.lbl_name.grid(row=1,column=0,padx=20,pady=20)
        self.entry_food = ctk.CTkEntry(frm,height=40,width=260,font=('Arial',30))
        self.entry_food.grid(row=1,column=1)
        self.dh1 = ctk.CTkLabel(frm,text="DH",font=('Arial',30))
        self.dh1.grid(row=1,column=2)

        self.lbl_name = ctk.CTkLabel(frm,text="Drink :",font=('Arial',30)) 
        self.lbl_name.grid(row=2,column=0,padx=20,pady=20)
        self.entry_drink = ctk.CTkEntry(frm,height=40,width=260,font=('Arial',30))
        self.entry_drink.grid(row=2,column=1)
        self.dh2 = ctk.CTkLabel(frm,text="DH",font=('Arial',30))
        self.dh2.grid(row=2,column=2)

        self.lbl_name = ctk.CTkLabel(frm,text="Entertainment :",font=('Arial',30)) 
        self.lbl_name.grid(row=3,column=0,padx=20,pady=20)
        self.entry_ent = ctk.CTkEntry(frm,height=40,width=260,font=('Arial',30))
        self.entry_ent.grid(row=3,column=1)
        self.dh3 = ctk.CTkLabel(frm,text="DH",font=('Arial',30))
        self.dh3.grid(row=3,column=2)

        self.lbl_name = ctk.CTkLabel(frm,text="Transport :",font=('Arial',30)) 
        self.lbl_name.grid(row=4,column=0,padx=20,pady=20)
        self.entry_tra = ctk.CTkEntry(frm,height=40,width=260,font=('Arial',30))
        self.entry_tra.grid(row=4,column=1)
        self.dh4 = ctk.CTkLabel(frm,text="DH",font=('Arial',30))
        self.dh4.grid(row=4,column=2)

        self.lbl_name = ctk.CTkLabel(frm,text="Other :",font=('Arial',30)) 
        self.lbl_name.grid(row=5,column=0,padx=20,pady=20)
        self.entry_other = ctk.CTkEntry(frm,height=40,width=260,font=('Arial',30))
        self.entry_other.grid(row=5,column=1)
        self.dh4 = ctk.CTkLabel(frm,text="DH",font=('Arial',30))
        self.dh4.grid(row=5,column=2)

        self.lbl = ctk.CTkLabel(frm,text="",font=('Arial',30),height=70) 
        self.lbl.grid(row=6,column=0)
        self.sb = ctk.CTkButton(frm,text="Submit",font=('Arial',30),width=200,height=60,command=self.display)
        self.sb.place(relx=0.4,rely=0.85)


    def display(self) :
            self.name = self.entry_name.get()
            self.food = int(self.entry_food.get())
            self.drink = int(self.entry_drink.get())
            self.ent = int(self.entry_ent.get())
            self.tra = int(self.entry_tra.get())
            self.other = int(self.entry_other.get())
            date = datetime.now()
            self.time = f"{date.day}-{date.month}-{date.year}"

            self.destroy()

            somme = self.food + self.drink + self.ent + self.tra + self.other
            self.per_food = (self.food*100) / somme
            self.per_drink = (self.drink*100) / somme
            self.per_ent = (self.ent*100) / somme
            self.per_tra = (self.tra*100) / somme
            self.per_other = (self.other*100) / somme

            self.save()

            y = np.array([self.per_food, self.per_drink, self.per_ent, self.per_tra, self.per_other])
            mylabels = ["Food", "Drink", "Entertainment", "Transport", "Other"]
            plt.pie(y, labels = mylabels)
            plt.title(f"Expense tracker : {self.name} ")
            ax_button = plt.axes([0.7, 0.05, 0.1, 0.075])  # Button position [x, y, width, height]
            button = Button(ax_button, 'History')
            button.on_clicked(self.show_info)
            plt.show()  
        

    def show_info(self, event):
        # Update the data or labels here if needed
        plt.close()
        app = ctk.CTk()
        #* initial window dimension :
        WIDTH = 1000
        HEIGHT = 500

        #* This code makes the window appear in the middle :
        screen_width = app.winfo_screenwidth()
        screen_height = app.winfo_screenheight()
        x = int((screen_width-WIDTH) / 2)
        y = int((screen_height-HEIGHT) / 2)

        app.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        app.resizable(False,False)
        app.title("Expense Tracker")
        table = ttk.Treeview(app)
        table["columns"] = (
            "Name",
            "Food",
            "Drink",
            "Entertainment",
            "Transport",
            "Other",
        )
        table.column("#0", width=0, stretch=tk.NO)
        table.column("Name", anchor=tk.CENTER, width=180)
        table.column("Food", anchor=tk.CENTER, width=180)
        table.column("Drink", anchor=tk.CENTER, width=180)
        table.column("Entertainment", anchor=tk.CENTER, width=180)
        table.column("Transport", anchor=tk.CENTER, width=180)
        table.column("Other", anchor=tk.CENTER, width=180)

        table.heading("#0", text="1", anchor=tk.CENTER)
        table.heading("Name", text="Name", anchor=tk.CENTER)
        table.heading("Food", text="Food", anchor=tk.CENTER)
        table.heading("Drink", text="Drink", anchor=tk.CENTER)
        table.heading("Entertainment", text="Entertainment", anchor=tk.CENTER)
        table.heading("Transport", text="Transport", anchor=tk.CENTER)
        table.heading("Other", text="Other", anchor=tk.CENTER)
        table.insert(parent='',index='end',iid=(0),text='',values=(self.name,self.food, self.drink, self.ent, self.tra, self.other))
        table.place(relx=0.08, rely=0.2)
        app.mainloop()

        




    def save(self) :
        file_exists = os.path.exists('data.txt')

        if not file_exists :
            f = open("data.txt","x",encoding='utf-8')
            f.close()
        f = open("data.txt","a",encoding='utf-8')
        f.write(f"Name:{self.name} at {self.time}\nFood:{self.food}DH\nDrink:{self.drink}DH\nEntertainment:{self.ent}DH\nTransport:{self.tra}DH\nOther:{self.other}DH\n")
        f.write('---------------------------------------------------------------------\n')
        f.close() 

        
app = App()
app.mainloop() 