import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
import time
import random




def forget_page1() :
    # clear
    lbl_select.place_forget()
    btn_player2.place_forget()
    btn_player3.place_forget()
    btn_player4.place_forget()


# game page

def stable_designe() :





    # style new window
    window.geometry('1500x800+10+15')

    # header
    global frm_header
    frm_header = Frame(width=1490,height=120,bg='#bbb')
    frm_header.place(x=5,y=0)

    # main
    global frm_main 
    frm_main = Frame(width=1490,height=520,bg='#888')
    frm_main.place(x=5,y=125)
    global tab_of_cordonne
    # ------------------------------------------------------------
    tab_of_cordonne = []
    stepss = 0
    for i in range(26,0,-2) :
        stepss += 1
        for j in range(0,8) :
            tab_of_cordonne.append([100+(i*50),(j*50)+90])
        if stepss %2 == 0 :
            tab_of_cordonne.append([100+((i-1)*50),90])
        else :
            tab_of_cordonne.append([100+((i-1)*50),90+(7*50)])
        if i == 2:
            for j in range(0,8) :
                tab_of_cordonne.append([100,(j*50)+90])

    for i in range(9,len(tab_of_cordonne),18):
        trev = []
        
        for j in range(i,i+8):
            trev.append(tab_of_cordonne[j])
        trev.reverse()
        for q in range(len(trev)):
            tab_of_cordonne[i+q] = trev[q]

    for q in range(len(tab_of_cordonne)) :
        all_steps = Frame(frm_main,height=50,width=50,bg='#8547ff',highlightbackground="#000",highlightthickness=1)
        all_steps.place(x=tab_of_cordonne[q][0],y=tab_of_cordonne[q][1])
        order_steps = Label(all_steps,text=str(f"{(q+1):03}"),font=('Arial',10),bg='#8547ff',fg='#ffffff')
        order_steps.place(x=12,y=15)
    tab_of_cordonne.append([80,55])

    # start step
    lbl_start = Label(frm_main,text='Start',font=('Arial',20),width=5,highlightbackground="#000",highlightthickness=1)
    lbl_start.place(x=1380,y=20)

    frm0 = Frame(frm_main,height=35,width=88,bg='#fff',highlightbackground="#000",highlightthickness=1)
    frm0.place(x=1380,y=55)





#   end step
    lbl_end = Label(frm_main,text='End',font=('Arial',20),width=5,highlightbackground="#000",highlightthickness=1)
    lbl_end.place(x=80,y=15)

    finall_step = Frame(frm_main,height=35,width=88,bg='#fff',highlightbackground="#000",highlightthickness=1)
    finall_step .place(x=80,y=55)

    # footer
    global frm_footer
    frm_footer = Frame(width=1490,height=150,bg='#555')
    frm_footer.place(x=5,y=650)
    





# -------------------------------------------------------
def var_designe() :

    global rem
    rem = 0
    global count_red
    count_red = []

    def move(frm_p) :
        if rem != 0 :
            frm_p.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_red.append(num)
        move(count_red)




        # To start move
        skipe = 0
        for k in range(len(count_red)) :
            skipe += count_red[k]



        if skipe == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                window.update()
                time.sleep(0.5)
                frm_p.place(x=(x+10),y=(y+10))
                lbl_num.pack()
                rem = 1



        # To play after start
        elif skipe > num :
            for j in range(skipe-num,skipe) :
                xx = tab_of_cordonne[j][0]
                yy = tab_of_cordonne[j][1]
                window.update()
                time.sleep(0.3)
                frm_p.place(x=(xx+10),y=(yy+10))
                lbl_num.pack()


# --------------------------------------------------------






    # def randomn(frk_p) :

global frm_player_green
global frm_player_red
global frm_player_blue
global frm_player_yellow
def role() :
    if numOfPlayer == 2 :
        x1 = 0
        # frame players
        frm_player_green.place_forget()
        frm_player1 = Frame(frm_main,height=30,width=30,bg='#0f0')
        lbl_num = Label(frm_player1,text='P1',font=('Arial',15),bg='#0f0',fg='#333')
        move(frm_p)
        x1 = 1
        if x1 == 1 :
            frm_player_red.place_forget()
            frm_player2 = Frame(frm_main,height=30,width=30,bg='#f00')
            lbl_num = Label(frm_player2,text='P2',font=('Arial',15),bg='#f00',fg='#333')
    elif numOfPlayer == 3 :
        # frame players
        frm_player_green.place_forget()
        frm_player1 = Frame(frm_main,height=30,width=30,bg='#0f0')
        lbl_num = Label(frm_player1,text='P1',font=('Arial',15),bg='#0f0',fg='#333')
        frm_player_red.place_forget()
        frm_player2 = Frame(frm_main,height=30,width=30,bg='#f00')
        lbl_num = Label(frm_player2,text='P2',font=('Arial',15),bg='#f00',fg='#333')
        frm_player_blue.place_forget()
        frm_player3 = Frame(frm_main,height=30,width=30,bg='#00f')
        lbl_num = Label(frm_player3,text='P3',font=('Arial',15),bg='#00f',fg='#333')
        

    elif numOfPlayer == 4 :
        # frame players
        frm_player_green.place_forget()
        frm_player1 = Frame(frm_main,height=30,width=30,bg='#0f0')
        lbl_num = Label(frm_player1,text='P1',font=('Arial',15),bg='#0f0',fg='#333')
        frm_player_red.place_forget()
        frm_player2 = Frame(frm_main,height=30,width=30,bg='#f00')
        lbl_num = Label(frm_player2,text='P2',font=('Arial',15),bg='#f00',fg='#333')
        frm_player_blue.place_forget()
        frm_player3 = Frame(frm_main,height=30,width=30,bg='#00f')
        lbl_num = Label(frm_player3,text='P3',font=('Arial',15),bg='#00f',fg='#333')
        frm_player_yellow.place_forget()
        frm_player4 = Frame(frm_main,height=30,width=30,bg='#ff0')
        lbl_num = Label(frm_player4,text='P4',font=('Arial',15),bg='#ff0',fg='#333')


        # careau player
    frm_player_green = Frame(frm_main,height=20,width=20,bg='#0f0')
    frm_player_green.place(x=1385,y=58)
    frm_player_red = Frame(frm_main,height=20,width=20,bg='#f00')
    frm_player_red.place(x=1405,y=58)
    frm_player_blue = Frame(frm_main,height=20,width=20,bg='#00f')
    frm_player_blue.place(x=1425,y=58)
    frm_player_yellow = Frame(frm_main,height=20,width=20,bg='#ff0')
    frm_player_yellow.place(x=1445,y=58)


    # Display result
lbl_result = Label(frm_footer,text='1...6',font=('Arial',20),height=2,width=5,relief="flat")
lbl_result.place(x=1210,y=35)
    # Button to move
dice_btn = Button(master=frm_footer,text='Move',font=('Arial',20),height=2,width=6,command=role,cursor='hand2')
dice_btn.place(x=1345,y=30)
frm_role = Frame(frm_header,height=55,width=55,bg='#888')
frm_role.place(x=1380,y=45)


# ------------------------------------------
global numOfPlayer
def sumfuns() :
    forget_page1()
    stable_designe()
    var_designe()
    role()




def players2() :
    sumfuns()
    numOfPlayer = 2




def players3() :
    sumfuns()
    numOfPlayer = 3
    


def players4() :
    sumfuns()
    numOfPlayer = 4
    







window = Tk()
window.title('Version 1.0')
window.geometry('550x350+500+200')
window.resizable(False, False)
window['bg'] = "#333"


# page1

lbl_select = Label(text='Select number of players :',font=('Arial',30),bg='#333',fg='#fff')
lbl_select.place(x=45,y=80)


btn_player2 = customtkinter.CTkButton(master=window,text='2 Players',corner_radius=40,font=('Arial',20),command=players2)
btn_player2.place(x=30,y=250)

btn_player3 = customtkinter.CTkButton(master=window,text='3 Players',corner_radius=40,font=('Arial',20),command=players3)
btn_player3.place(x=200,y=250)

btn_player4 = customtkinter.CTkButton(master=window,text='4 Players',corner_radius=40,font=('Arial',20),command=players4)
btn_player4.place(x=370,y=250)



# page2
# page3

window.mainloop()
