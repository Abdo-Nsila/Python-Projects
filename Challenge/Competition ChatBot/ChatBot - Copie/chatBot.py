from tkinter import *
import tkinter
import customtkinter

BACKGROUND_COLOR = "#444"
TEXT_COLOR = '#fff'
WINDOW_HEIGHT = 550
WINDOW_WIDTH = 750

window = Tk()
window.iconbitmap('chatbot.ico')
window.title("ChatBot")
window.resizable(False, False)
window['bg'] = '#444'

#* Get window and screen info
window_width = WINDOW_WIDTH

window_height = WINDOW_HEIGHT

screen_width = window.winfo_screenwidth()

screen_height = window.winfo_screenheight()

#* Center a window
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

def start() :
    lbl_welc.pack_forget()
    lbl_name.pack_forget()
    entry.pack_forget()
    btn.pack_forget()
    window_width = 1200
    window_height = 650
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    name = entry.get()
    
    


#* Add element inside window
main_page = Frame(window, bg=BACKGROUND_COLOR, height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
main_page.pack()

lbl_welc = Label(main_page,bg=BACKGROUND_COLOR,fg=TEXT_COLOR ,text="Bienvenue sur notre chatbot d'orientation !\n Pour commencer, veuillez répondre aux\n questions suivantes pour nous aider\n à mieux comprendre vos intérêts,\n vos compétences et vos motivations. Nous utiliserons\n ces informations pour vous suggérer des options\n de carrière qui correspondent à votre personnalité.\n Nous vous remercions d'avance pour votre participation !", font=('consolas', 15))
lbl_welc.pack(pady=50)

lbl_name = Label(text=' Enter your name : ', font=('consolas', 20),bg=BACKGROUND_COLOR,fg=TEXT_COLOR)
lbl_name.pack()
entry = Entry(width=50,highlightthickness=2,highlightbackground='#ff0',justify='center')
entry.pack(pady=20)
btn = Button(text="START",font=('consolas', 20),command=start)
btn.pack()









# lbl_welc = Label(window,text="Bienvenue sur notre chatbot d'orientation ! Pour commencer, veuillez répondre aux questions suivantes pour nous aider à mieux comprendre vos intérêts, vos compétences et vos motivations. Nous utiliserons ces informations pour vous suggérer des options de carrière qui correspondent à votre personnalité. Nous vous remercions d'avance pour votre participation !")
# lbl_welc.pack()




window.mainloop()