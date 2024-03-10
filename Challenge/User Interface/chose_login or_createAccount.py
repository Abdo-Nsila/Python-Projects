import customtkinter
import tkinter
import os


customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green


window = customtkinter.CTk() # creating custom tkinter window
#* initial window dimension :
WIDTH = 600
HEIGHT = 400

#* This code makes the window appear in the middle :
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width-WIDTH) / 2)
y = int((screen_height-HEIGHT) / 2)

window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
window.resizable(False,False)
window.title("Welcome")

frame = customtkinter.CTkFrame(master=window , corner_radius= 10 , height=350, width=550)
frame.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)


def login() :
    window.destroy()
    os.system('python login.py')
def account() :
    window.destroy()
    os.system('python account.py')

# window.wm_attributes('-transparentcolor', '#333') 

lbl = customtkinter.CTkLabel(master=frame , text="Welcome" , font=('Centry Gothic',45))
lbl.place(relx=0.5,rely=0.25,anchor=tkinter.CENTER)

btn1 = customtkinter.CTkButton(master=frame , height=40 , width=240 , text='Login' , corner_radius=7 , command=login , font=('Arial',20))
btn1.place(relx=0.5 , rely=0.58 , anchor=tkinter.CENTER)

btn2 = customtkinter.CTkButton(master=frame , height=40 , width=240 , text='Create Account' , corner_radius=7 , command=account , font=('Arial',20))
btn2.place(relx=0.5 , rely=0.75 , anchor=tkinter.CENTER)

window.mainloop()