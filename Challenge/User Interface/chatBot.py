import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkcalendar import DateEntry
# import winsound

customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green

app = customtkinter.CTk() # creating custom tkinter window
app.geometry("800x700")
app.resizable(False,False)
app.title("Login")

def add() :
    
    lbl3 = customtkinter.CTkLabel(master=new_window , text="Nice Bro" , font=("Centry Gothic",60),text_color='#0f8')
    lbl3.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)



def start()  :
    # winsound.Beep(1500 , 100)
    global new_window
    username = entry1.get()
    password = entry2.get()
    coche = check_var.get()

    app.destroy()
    new_window = customtkinter.CTk() #* creating custom tkinter window
    new_window.geometry("1280x720")
    new_window.title("Welcome")

    lbl1 = customtkinter.CTkLabel(master=new_window , text=f"Username: {username}" , font=("Centry Gothic",60),text_color='#ff0')
    lbl1.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

    lbl2 = customtkinter.CTkLabel(master=new_window , text=f"Password: {password}" , font=("Centry Gothic",60),text_color='#f90')
    lbl2.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

    lbl3 = customtkinter.CTkLabel(master=new_window , text=f"{coche}" , font=("Centry Gothic",60),text_color='#f0f')
    lbl3.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)

    add()

    new_window.mainloop()



frame = customtkinter.CTkFrame(master=app , corner_radius= 20)
frame.pack(padx=200, pady=80 , anchor=tkinter.CENTER , fill='both',expand=True)
 

lbl2 = customtkinter.CTkLabel(master=frame , text="Log into your Account" , font=('Centry Gothic',20))
lbl2.place(relx=0.5,rely=0.2,anchor=tkinter.CENTER)


entry1 = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Username')
entry1.place(relx=0.5,rely=0.35,anchor=tkinter.CENTER)


entry2 = customtkinter.CTkEntry(master=frame , height=35, width=240 , placeholder_text='Password')
entry2.place(relx=0.5,rely=0.45,anchor=tkinter.CENTER)

# cal=DateEntry(frame,selectmode='day',date_pattern='MM-dd-yyyy')
# cal.place(relx=0.5,rely=0.6,anchor=tkinter.CENTER)
def login() :
    pass
def account() :
    pass

btn1 = customtkinter.CTkButton(master=frame , height=40 , width=240 , text='Login' , corner_radius=7 , command=login , font=('Arial',20))
btn1.place(relx=0.5 , rely=0.6 , anchor=tkinter.CENTER)

btn2 = customtkinter.CTkButton(master=frame , height=40 , width=240 , text='Create Account' , corner_radius=7 , command=account , font=('Arial',20))
btn2.place(relx=0.5 , rely=0.75 , anchor=tkinter.CENTER)







app.mainloop()
