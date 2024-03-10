from tkinter import *
import random

cond = False

def random1():
    num = random.randint(1, 10)
    if ((int(lblPR['text']) < 10) and (int(lblPL['text']) < 10)) :
        lbl1['text'] = str(int(num))
    return num


def random2():
    num = random.randint(1, 10)
    if ((int(lblPR['text']) < 10) and (int(lblPL['text']) < 10)) :
        lbl2['text'] = str(int(num))
    return num


def Play():
    p1 = random1()
    p2 = random2()
    if p1 > p2:
        # lbl3['text'] = str('Player 1  WIN')
        win = 'player1'
        return win
    elif p2 > p1:
        # lbl3['text'] = str('Player 2  WIN')
        win = 'player2'
        return win



def Score():
    set1 = {'      Hhhhh        ','        Go bro          ','          Flex...          ','        PcGamer           ','        Nice         ','       Oh         ','        ok          '}
    for i in set1 :
        lbl3 ['text'] = i
    score = Play()
    if score == 'player1' and ((int(lblPR['text']) < 10) and (int(lblPL['text']) < 10))  :
        lblPR['text'] = str(int(lblPR['text']) + 1)
    elif score == 'player2' and ((int(lblPR['text']) < 10) and (int(lblPL['text']) < 10)) :
        lblPL['text'] = str(int(lblPL['text']) + 1)
    if int(lblPR['text']) == 10 :
        lbl3['text'] = str('Player 1 WIN')
    elif int(lblPL['text']) == 10 :
        lbl3['text'] = str('Player 2 WIN')


def Restart() :
    # Display Statut
    lbl3 ['text'] = str('        Start      ')
    # Reset Random
    lbl1['text'] = str(int(0))
    lbl2['text'] = str(int(0))
    # Reset Score
    lblPR['text'] = str(int(0))
    lblPL['text'] = str(int(0))
    


# Make a Window
window = Tk()
window.title('ABDELLAH')
window.geometry('900x550+350+150')
window.resizable(False, False)
window['bg'] = "#334"


# Left of Score Player 2
frL = Frame(width='250', height='100', bg='#fff')
frL.place(x=0, y=1)
frL1 = Frame(width='240', height='90', bg='red')
frL1.place(x=5, y=5)
# Score
lblL = Label(frL1, text='Score of player 2 :', font=('Arial', 13), bg='red')
lblL.place(x=60, y=15)
lblPL = Label(frL1, text='0', font=('Arial', 30), bg='red')
lblPL.place(x=110, y=35)


# Center of Result
frm = Frame(width='400', height='100', bg='#000')
frm.place(x=250, y=1)
frm1 = Frame(width='380', height='80', bg='orange')
frm1.place(x=260, y=10)
# Display Result
lbl3 = Label(frm1, text='        Start      ', font=('Arial', 30), background='orange')
lbl3.place(x=60, y=15)


# Right of Score Player 1
frR = Frame(width='250', height='100', bg='#fff')
frR.place(x=650, y=1)
frR1 = Frame(width='240', height='90', bg='blue')
frR1.place(x=655, y=5)
# Score
lblR = Label(frR1, text='Score of player 1 :', font=('Arial', 13), bg='blue')
lblR.place(x=60, y=15)
lblPR = Label(frR1, text='0', font=('Arial', 30), bg='blue')
lblPR.place(x=110, y=35)


# Between
fr1 = Frame(width='400', height='400', bg='#000')
fr11 = Frame(width='380', height='380', bg='#bbb')
fr11.place(x=260, y=110)
# Button Play
bt1 = Button(fr11, text='Play', height=2, width=20, fg='#0f0', bg='#fff', font=30,activebackground='#0f0', activeforeground='#fff', bd=3, cursor='mouse' ,command=Score)
bt1.place(x=80, y=80)
# Button Restart
bt2 = Button(fr11, text='Restart', height=2, width=20, fg='#f00', bg='#fff',font=30, activebackground='#f00', activeforeground='#fff', bd=3,command=Restart)
bt2.place(x=80, y=180)
# Button Quit
bt3 = Button(fr11, text='Exit', height=2, width=20, fg='#000', bg='#fff',font=30, activebackground='#000', activeforeground='#fff', bd=3,command=window.quit)
bt3.place(x=80, y=280)

# Player 1
fr2 = Frame(width='250', height='400', bg='#00f')
fr2.place(x=650, y=100)
fr21 = Frame(width='230', height='380', bg='#bbb')
fr21.place(x=660, y=110)

# Random 1
lbl1 = Label(fr21, text='0', font= ('Arial' , 80), background='#556')
lbl1.place(x=80, y=100)


# Player 2
fr0 = Frame(width='250', height='400', bg='#f00')
fr0.place(x=0, y=100)
fr01 = Frame(width='230', height='380', bg='#bbb')
fr01.place(x=10, y=110)

# Random 2
lbl2 = Label(fr01, text='0', font=('Arial', 80), background='#556')
lbl2.place(x=80, y=100)


window.mainloop()
