import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
import random


def fun() :
    a = random.randint(100, 1500)
    window.geometry('')


window = Tk()
window.title('Version 1.0')
# window.iconbitmap('code.ico')
window.geometry('700x350')
window.resizable(False, False)
window['bg'] = "#333"




btn_word = customtkinter.CTkButton(master=window,text='Submit',corner_radius=40,font=('Arial',20),command=fun)
btn_word.place(x=110,y=100)






window.mainloop()