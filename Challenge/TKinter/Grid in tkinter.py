from tkinter import *

window = Tk()
window.title('Horloge')
window.geometry('800x600+350+100')
window.resizable(False, False)
window['bg'] = '#333'


display = Text(height=5, font=('Arial', 16))
display.pack(padx=50, pady=50)

frm1 = Frame(width=700, height=380, bg='#fff')
frm1.place(x=50, y=180)


btn1 = Button(frm1,text='1',font=('Arial',50),bg='#ff0',height=2,width=5,)
btn1.grid(row=0,column=0)

btn2 = Button(frm1,text='2',font=('Arial',50),bg='#ff0',height=2,width=5)
btn2.grid(row=0,column=1)


btn3 = Button(frm1,text='3',font=('Arial',50),bg='#ff0',height=2,width=5)
btn3.grid(row=1,column=0)

btn4 = Button(frm1,text='4',font=('Arial',50),bg='#ff0',height=2,width=5)
btn4.grid(row=1,column=1)


window.mainloop()
