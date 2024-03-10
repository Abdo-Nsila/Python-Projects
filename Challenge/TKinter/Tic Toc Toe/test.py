from tkinter import *
import random



def create_base() :
    global Tab_btn
    btn1=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn1)
    btn2=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn2)
    btn3=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn3)
    btn4=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn4)
    btn5=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn5)
    btn6=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn6)
    btn7=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn7)
    btn8=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn8)
    btn9=Button(master=frm_game,text=' ',font=('Arial',50),height=2,width=5,command=next_turn9)
    Tab_btn = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9]
    n = -1
    for i in range(3) :
        for j in range(3) :
            n += 1
            Tab_btn[n].grid(row=i,column=j)
            (Tab_btn[n])['bg'] = '#fff'

def random_player() :
    global check
    check = True
    t = ['O','X']
    r = random.randint(0,1)
    exp = t[r] 
    lbl_player['text'] = str('Player : ' +  exp)
    lbl_role['text'] = exp 


def change_turn(btn) :
    global win
    global Tab_btn
    global check
    if check == True :
        if lbl_role['text'] == 'O' :
            btn['text'] = 'O'
            btn['fg'] = '#00f' 
            lbl_role['text'] = 'X'
            lbl_player['text'] = str('Player : X')
            check = False
        elif lbl_role['text'] == 'X' :
            btn['text'] = 'X'
            btn['fg'] = '#f00'
            lbl_role['text'] = 'O'
            lbl_player['text'] = str('Player : O')
            check = False
    elif lbl_role['text'] == 'O' :
        btn['text'] = 'O'
        btn['fg'] = '#00f'
        if win == False :
            lbl_player['text'] = str('Player : X')
        check_win(btn)
        lbl_role['text'] = 'X'
    elif lbl_role['text'] == 'X' :
        btn['text'] = 'X'
        btn['fg'] = '#f00'
        if win == False :
            lbl_player['text'] = str('Player : O')
        check_win(btn)
        lbl_role['text'] = 'O'

win = False
def check_win(btn) : 
    global win
    # HORIZONTAL
    if ((Tab_btn[0])['text']) == ((Tab_btn[1])['text']) == ((Tab_btn[2])['text']) and (Tab_btn[0])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[0])['bg'] = '#0f0'
        (Tab_btn[1])['bg'] = '#0f0'
        (Tab_btn[2])['bg'] = '#0f0'
    elif ((Tab_btn[3])['text']) == ((Tab_btn[4])['text']) == ((Tab_btn[5])['text']) and (Tab_btn[3])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[3])['bg'] = '#0f0'
        (Tab_btn[4])['bg'] = '#0f0'
        (Tab_btn[5])['bg'] = '#0f0'
    elif ((Tab_btn[6])['text']) == ((Tab_btn[7])['text']) == ((Tab_btn[8])['text']) and (Tab_btn[6])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[6])['bg'] = '#0f0'
        (Tab_btn[7])['bg'] = '#0f0'
        (Tab_btn[8])['bg'] = '#0f0'
    # VERTICAL
    elif ((Tab_btn[0])['text']) == ((Tab_btn[3])['text']) == ((Tab_btn[6])['text']) and (Tab_btn[0])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[0])['bg'] = '#0f0'
        (Tab_btn[3])['bg'] = '#0f0'
        (Tab_btn[6])['bg'] = '#0f0'
    elif ((Tab_btn[1])['text']) == ((Tab_btn[4])['text']) == ((Tab_btn[7])['text']) and (Tab_btn[1])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[1])['bg'] = '#0f0'
        (Tab_btn[4])['bg'] = '#0f0'
        (Tab_btn[7])['bg'] = '#0f0'
    elif ((Tab_btn[2])['text']) == ((Tab_btn[5])['text']) == (((Tab_btn[8])['text'])) and (Tab_btn[2])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[2])['bg'] = '#0f0'
        (Tab_btn[5])['bg'] = '#0f0'
        (Tab_btn[8])['bg'] = '#0f0'
    # OBLIQUE
    elif ((Tab_btn[0])['text']) == ((Tab_btn[4])['text']) == ((Tab_btn[8])['text']) and (Tab_btn[0])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[0])['bg'] = '#0f0'
        (Tab_btn[4])['bg'] = '#0f0'
        (Tab_btn[8])['bg'] = '#0f0'
    elif ((Tab_btn[2])['text']) == ((Tab_btn[4])['text']) == (((Tab_btn[6])['text'])) and (Tab_btn[2])['text'] != ' ' and win == False :
        win = True
        lbl_player['text'] = 'Player ' + lbl_role['text'] + ' WIN'
        lbl_player['bg'] = btn['fg']
        (Tab_btn[2])['bg'] = '#0f0'
        (Tab_btn[4])['bg'] = '#0f0'
        (Tab_btn[6])['bg'] = '#0f0'
    # EQUAL RESULT
    equal = True
    for i in range(len(Tab_btn)) :
        if (Tab_btn[i])['text'] == ' ' :
            equal = False
    if equal == True and win == False :
        lbl_player['text'] = 'Equal'
        for j in range(len(Tab_btn)) :
            (Tab_btn[j])['bg'] = '#000'


def next_turn1() :
    if Tab_btn[0]['text'] == ' ' :
        change_turn(Tab_btn[0])
def next_turn2() :
    if Tab_btn[1]['text'] == ' ' :
        change_turn(Tab_btn[1])
def next_turn3() :
    if Tab_btn[2]['text'] == ' ' :
        change_turn(Tab_btn[2])
def next_turn4() :
    if Tab_btn[3]['text'] == ' ' :
        change_turn(Tab_btn[3])
def next_turn5() :
    if Tab_btn[4]['text'] == ' ' :
        change_turn(Tab_btn[4])
def next_turn6() :
    if Tab_btn[5]['text'] == ' ' :
        change_turn(Tab_btn[5])
def next_turn7() :
    if Tab_btn[6]['text'] == ' ' :
        change_turn(Tab_btn[6])
def next_turn8() :
    if Tab_btn[7]['text'] == ' ' :
        change_turn(Tab_btn[7])
def next_turn9() :
    if Tab_btn[8]['text'] == ' ' :
        change_turn(Tab_btn[8])

def restart() :
    global check
    global win
    global equal
    check = False
    win = False
    equal = True
    lbl_player['bg'] = '#eee'
    random_player()
    for i in Tab_btn :
        i['text'] = ' '
        i['bg'] = '#fff'



window = Tk()
window.geometry("900x700+300+50")
window.resizable(False,False)


frm_game = Frame(height=700,width=500,bg='#555')
frm_game.place(x=150,y=100)
lbl_role = Label(text=' ')
lbl_player = Label(text='Player : ?',font=('Arial',50))
random_player()
lbl_player.pack()
btn_resart = Button(text='Restart',font=('Arial',30),fg='#00f',command=restart)
btn_resart.place(x=50,y=10)
btn_quit = Button(text='   Exit   ',font=('Arial',30),fg='#f00',command=quit)
btn_quit.place(x=680,y=10)
create_base()



window.mainloop()
