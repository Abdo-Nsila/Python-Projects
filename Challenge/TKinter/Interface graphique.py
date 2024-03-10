# from tkinter import *
# interface = Tk()
# interface.iconbitmap("code.ico")
# interface.title("NSILA")
# interface.geometry("1000x550")
# interface.minsize(650,400)
# interface.mainloop()


# import time
# t = 0
# while True :
#     time.sleep(1)
#     t += 1
#     print(t)


import tkinter as tk
import time
from gtts import gTTS
from playsound import playsound

def Somme():
    # text0 = str(input("Entrer une phrase : "))
    # text0 = 'Hello'
    # textsound = gTTS(text = text0)
    # textsound.save('welcome.mp3')
    # playsound('welcome.mp3')
    lbl1['text'] = str(int(lbl1['text']) + 1)


def Sub():
    # text0 = 'siiiiiiiiiiiiiiiiiiiiiuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuur'
    # textsound = gTTS(text = text0)
    # textsound.save('welcome.mp3')
    # playsound('welcome.mp3')
    lbl1['text'] = str(int(lbl1['text']) - 1)


window = tk.Tk()
# window.iconbitmap("code.ico")
window['bg'] = "#556"
window.title("NSILA")
window.geometry("1000x550+250+150")
# window.resizable(False , True)
window.minsize(650, 400)



lbl1 = tk.Label(text='0', font=('Arial', 100), background='#556')
lbl1.pack()

somme = tk.Button(text='Click to add', command=Somme, font=('Arial', 50), background='#0f0')
somme.pack()

sub = tk.Button(text='Click to sub', command=Sub, font=('Arial', 50), background='#f00')
sub.pack()

# img = tk.PhotoImage('C:\\Users\\aa\Desktop\\Challenge\\goku.png')
# goku = tk.Label(image=img, width=200,height=200)
# goku.pack()

enter = tk.Entry(width=50)
enter.pack()

window.mainloop()

