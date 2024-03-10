




from tkinter import *



def add() :
    lbl1['text'] = str(int(lbl1['text']) + 1)
def sub() :
    lbl1['text'] = str(int(lbl1['text']) - 1)


# Make a window
window = Tk()
window.title('Game')
window.geometry('900x550+350+150')
window.resizable(False, False)
window['bg'] = '#aaa'

frm1 = Frame(width='450',height='550',bg='#0f0')
frm1.place(x=0,y=0)
frm2 = Frame(width='450',height='550',bg='#00f')
frm2.place(x=450,y=0)


lbl1 = Label(frm1,text='0', font = ('Arial' , 80), bg='#00f', fg='#0f0')
lbl1.place(x=0, y=0)

lbl2 = Label(frm2,text='Hello\nAnas', font= ('Arial' , 10), bg='#f00', fg='#00f')
lbl2.place(x=0, y=0)

btn0 = Button(frm1,text='Click me to add', height=2, width=20,bg='#fff',fg='#000',font=5,activebackground='#0f0',activeforeground='red',bd=5,command=add,cursor='mouse')
btn0.place(x=0, y=200)
btn1 = Button(frm1,text='Click me too sub', height=2, width=20,bg='#000',fg='#fff',font=5,activebackground='#0f0',activeforeground='red',bd=5,command=sub)
btn1.place(x=0, y=400)

btn2 = Button(frm2,text='Click me', height=2, width=20,bg='#000',fg='#fff',font=5,activebackground='#0f0',activeforeground='red',bd=5)
btn2.place(x=0, y=50)

ent1 = Entry(frm1,justify='center',font=('Arial', 15))
ent1.place(x=150)



window.mainloop()
