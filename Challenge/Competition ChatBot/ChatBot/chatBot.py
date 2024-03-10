import tkinter
import customtkinter
from PIL import ImageTk, Image
# import winsound

customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green

app = customtkinter.CTk() # creating custom tkinter window
app.geometry("800x700")
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




# img1 = ImageTk.PhotoImage(Image.open('pattern.png'))
# lbl1 = customtkinter.CTkLabel(master=app, image=img1, text="")
# lbl1.pack()


frame = customtkinter.CTkFrame(master=app , corner_radius= 20)
frame.pack(padx=200, pady=80 , anchor=tkinter.CENTER , fill='both',expand=True)
# frame = customtkinter.CTkFrame(master=app , width=320 , height=360 , corner_radius= 20)
# frame.pack(padx=50, pady=10 , fill='both',expand=True)
 

lbl2 = customtkinter.CTkLabel(master=frame , text="Log into your Account" , font=('Centry Gothic',20))
lbl2.place(relx=0.5,rely=0.25,anchor=tkinter.CENTER)


entry1 = customtkinter.CTkEntry(master=frame , width=220 , placeholder_text='Username')
entry1.place(relx=0.5,rely=0.35,anchor=tkinter.CENTER)


entry2 = customtkinter.CTkEntry(master=frame , width=220 , placeholder_text='Password')
entry2.place(relx=0.5,rely=0.45,anchor=tkinter.CENTER)



#* check_var = tkinter.IntVar()
check_var = tkinter.StringVar()
check_var.set("OFF")
# def checkbox_event():
#     print("checkbox toggled, current value:", check_var.get())
check = customtkinter.CTkCheckBox(master=frame , text='Remember me' , font=('Centry Gothic',13) , text_color='#0d8',variable=check_var, onvalue="ON", offvalue="OFF")
check.place(relx=0.35,rely=0.55,anchor=tkinter.CENTER)


lbl3 = customtkinter.CTkLabel(master=frame , text="Forget password" , font=('Centry Gothic',13) , text_color='#0d8')
lbl3.place(relx=0.65,rely=0.55,anchor=tkinter.CENTER)


btn1 = customtkinter.CTkButton(master=frame , width=220 , text='Login' , corner_radius=7 , command=start)
btn1.place(relx=0.5 , rely=0.65 , anchor=tkinter.CENTER)

img2 = ImageTk.PhotoImage(Image.open('D:/Files/SCHOOL/Python/Challenge/Competition ChatBot/ChatBot/google.png').resize((20,20)), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(Image.open('D:/Files/SCHOOL/Python/Challenge/Competition ChatBot/ChatBot/facebook.png').resize((20,20)), Image.ANTIALIAS)

btn2 = customtkinter.CTkButton(master=frame , height=30 , width=100 , image=img2 , text='Login Google' , corner_radius=5 , text_color='#000' , fg_color='#fff' , hover_color="#0d8")
btn2.place(relx=0.35,rely=0.75,anchor=tkinter.CENTER)
btn3 = customtkinter.CTkButton(master=frame , height=30 , width=100 , image=img3 , text='Login Facebook' , corner_radius=5 , text_color='#000' , fg_color='#fff' , hover_color="#0d8")
btn3.place(relx=0.7,rely=0.75,anchor=tkinter.CENTER)




# frm0 = customtkinter.CTkFrame(master=app)
# frm0.pack(padx=20,pady=50,fill='both',expand=True)

# frm1 = customtkinter.CTkFrame(master=app)
# frm1.pack(padx=20,pady=50,fill='both',expand=True)

# frm2 = customtkinter.CTkFrame(master=app)
# frm2.pack(padx=20,pady=50,fill='both',expand=True)

# btn = customtkinter.CTkButton(master=frm0,text='Click me')
# btn.place(x=20,y=20)



app.mainloop()
