from tkinter import *
from tkinter import messagebox

import time
import datetime
import os


def horloge():

    H = int(hourEntry.get())
    M = int(minuteEntry.get())
    S = int(secondEntry.get())

    while True :
        window.update()
        time.sleep(1)
        if (S < 59 and M < 59 and H < 23) or (S < 59 and M == 59 and H < 23) or (S < 59 and M < 59 and H == 23) or (S < 59 and M == 59 and H == 23):
            S = S + 1
        elif S == 59 and M < 59 and H < 23:
            S = 0
            M = M + 1
        elif S == 59 and M == 59 and H < 23:
            S = 0
            M = 0
            H = H + 1
            messagebox.showinfo("This is a " + str(f"{H:02}" + "o'clock"))
        elif S == 59 and M == 59 and H == 23:
            S = 0
            M = 0
            H = 00
            messagebox.showerror("This is a " + str(f"{H:02}" + "o'clock"))

        hour.set(f"{H:02}" + " :")
        minute.set(f"{M:02}" + " :")
        second.set(f"{S:02}")



window = Tk()
window.title('Horloge')
window.geometry('800x500+350+100')
window.resizable(False,False)
window['bg'] = '#333'

hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("00")
minute.set("00")
second.set("00")


frm1 = Frame(width=500,height=200,bg='#333')
frm1.place(x=120,y=150)

hourEntry = Entry(frm1,textvariable=hour,font=('Arial',60),bg='#44c',fg='#fff')
hourEntry.place(x=40,y=50)

minuteEntry = Entry(frm1,textvariable=minute,font=('Arial',60),bg='#44e',fg='#fff')
minuteEntry.place(x=190,y=50)

secondEntry = Entry(frm1,textvariable=second,font=('Arial',60),bg='#44f',fg='#fff')
secondEntry.place(x=350,y=50)

btn = Button(text='Enter a value of clock',font=('Arial',13),bg='#a3f',fg='#fff',command=horloge)
btn.place(x=310,y=400)


window.mainloop()
