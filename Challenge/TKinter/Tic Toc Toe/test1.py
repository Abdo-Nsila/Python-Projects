from tkinter import *

def get_display() :
    a = ent.get()
    lbl_display['text'] = str(a)

window = Tk()
window.title('Horloge')
window.geometry('800x600+350+100')
window.resizable(False, False)
window['bg'] = '#333'

ent = Entry(font=('Arial',50),justify='center') 
ent.pack()

btn = Button(text='Click me',command=get_display)
btn.pack()

lbl_display = Label(text=' ',font=('Arial',50))
lbl_display.pack()

window.mainloop()