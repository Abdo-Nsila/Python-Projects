import tkinter
import customtkinter
from PIL import ImageTk, Image
import winsound

customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green

app = customtkinter.CTk() # creating custom tkinter window
app.geometry("800x500")
app.title("Login")


frame = customtkinter.CTkFrame(master=app , corner_radius= 20)
frame.pack(anchor=tkinter.CENTER , fill='both',expand=True)

img1 = ImageTk.PhotoImage(Image.open('pattern.png'))
lbl1 = customtkinter.CTkLabel(master=frame , image=img1 , text="")
lbl1.pack()


frm0 = customtkinter.CTkFrame(master=lbl1)
frm0.place(relx=0.4,rely=0.3)


# frm0 = customtkinter.CTkFrame(master=frame)
# frm0.pack(padx=20,pady=50,fill='both',expand=True)

# frm1 = customtkinter.CTkFrame(master=frame)
# frm1.pack(padx=20,pady=50,fill='both',expand=True)

# frm2 = customtkinter.CTkFrame(master=frame)
# frm2.pack(padx=20,pady=50,fill='both',expand=True)

# btn = customtkinter.CTkButton(master=frm0,text='Click me')
# btn.place(x=20,y=20)



app.mainloop()
