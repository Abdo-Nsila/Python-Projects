import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
import time
import random
import winsound


def forget_page1():
    # clear
    lbl_select.place_forget()
    btn_player2.place_forget()
    btn_player3.place_forget()
    btn_player4.place_forget()


def forget_page1():
    # clear
    lbl_select.place_forget()
    btn_player2.place_forget()
    btn_player3.place_forget()
    btn_player4.place_forget()


# game page
def stable_designe():
    # style new window
    window.geometry('1500x800+10+15')

    # ______________________________________________/header\________________________________________________
    global frm_header
    frm_header = Frame(width=1490, height=120, bg='#bbb')
    frm_header.place(x=4, y=0)

    # ______________________________________________/main\________________________________________________
    global frm_main
    frm_main = Frame(width=1490, height=520, bg='#888')
    frm_main.place(x=4, y=125)
    global tab_of_cordonne
    # ------------------------------------------------------------
    tab_of_cordonne = []
    stepss = 0
    for i in range(26, 0, -2):
        stepss += 1
        for j in range(0, 8):
            tab_of_cordonne.append([100+(i*50), (j*50)+90])
        if stepss % 2 == 0:
            tab_of_cordonne.append([100+((i-1)*50), 90])
        else:
            tab_of_cordonne.append([100+((i-1)*50), 90+(7*50)])
        if i == 2:
            for j in range(0, 8):
                tab_of_cordonne.append([100, (j*50)+90])

    for i in range(9, len(tab_of_cordonne), 18):
        trev = []

        for j in range(i, i+8):
            trev.append(tab_of_cordonne[j])
        trev.reverse()
        for q in range(len(trev)):
            tab_of_cordonne[i+q] = trev[q]

    for q in range(len(tab_of_cordonne)):
        all_steps = Frame(frm_main, height=50, width=50, bg='#8547ff', highlightbackground="#000", highlightthickness=1)
        all_steps.place(x=tab_of_cordonne[q][0], y=tab_of_cordonne[q][1])
        order_steps = Label(all_steps, text=str(f"{(q+1):03}"), font=('Arial', 10), bg='#8547ff', fg='#ffffff')
        order_steps.place(x=12, y=15)
    tab_of_cordonne.append([80, 55])

    # Start step
    lbl_start = Label(frm_main, text='Start', font=('Arial', 20), width=5,highlightbackground="#000", highlightthickness=1)
    lbl_start.place(x=1380, y=20)

    frm0 = Frame(frm_main, height=35, width=88, bg='#fff', highlightbackground="#000", highlightthickness=1)
    frm0.place(x=1380, y=55)

#  End step
    lbl_end = Label(frm_main, text='End', font=('Arial', 20), width=5, highlightbackground="#000", highlightthickness=1)
    lbl_end.place(x=80, y=15)

    finall_step = Frame(frm_main, height=35, width=88, bg='#fff', highlightbackground="#000", highlightthickness=1)
    finall_step .place(x=80, y=55)
    global frm_final_place
    frm_final_place = Frame(frm_main,height=520,width=75,bg='#ccc')
    frm_final_place.place(x=0,y=0)

    #  ________________________________________________/footer\________________________________________________
    global frm_footer
    frm_footer = Frame(width=1490, height=150, bg='#555')
    frm_footer.place(x=4, y=650)














def sumfuns():
    forget_page1()
    stable_designe()


    # Global variables :

def players2():
    sumfuns()
    numOfPlayer = 2
    # ______________________________________________/header\___________________________________________________


    # ______________________________________________/main\___________________________________________________
        # Careau player
    frm_player_green = Frame(frm_main, height=30, width=30, bg='#0f0',highlightthickness=2,highlightbackground='#000')
    frm_player_green.place(x=1390, y=58)
    frm_player_red = Frame(frm_main, height=30, width=30, bg='#f00',highlightthickness=2,highlightbackground='#000')
    frm_player_red.place(x=1430, y=58)

        # order place
    frm_first_player= Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_first_player.place(x=10, y=30)
    a = frm_first_player['bg']
    lbl_first_player = Label(frm_first_player,text='1',font=('Arial',20),bg=a)
    lbl_first_player.place(x=10,y=2)

    frm_second_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_second_player.place(x=10, y=100)
    b = frm_second_player['bg']
    lbl_second_player = Label(frm_second_player,text='2',font=('Arial',20),bg=b)
    lbl_second_player.place(x=10,y=2)
    # ______________________________________________/footer\___________________________________________________
        # Display result
    lbl_result = Label(frm_header,text='1...6',font=('Arial',20),height=2,width=4,relief="flat",bg='#000',fg='#fff',highlightthickness=4,highlightbackground='#fff')
    lbl_result.place(x=1200,y=10)






    global count_green
    count_green = []
    global count_red
    count_red = []


    def role2_1() :
        
        # Tritement du Role :
        # frm_player_green.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_green.append(num)
        window.update()
        time.sleep(0.1)

        num_of_case = 0
        for i in count_green :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_green.place(x=x+10,y=y+10)
                winsound.Beep(250, 100)
                window.update()
                time.sleep(0.4)
                
        else:
            for j in range(num_of_case-num,num_of_case) :
                # winsound.Beep(250, 100) 
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777'):
                    # winsound.Beep(100, 1000)
                    frm_player_green.place(x=90,y=55)
                    frm_first_player['bg'] = '#0f0'
                    lbl_first_player['bg'] = '#0f0'
                    frm_second_player['bg'] = '#f00'
                    lbl_second_player['bg'] = '#f00'
                    dice_btn1.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] == '#f00') :
                    frm_player_green.place(x=90,y=55)
                    dice_btn1.place_forget()
                else :
                    frm_player_green.place(x=x+10,y=y+10)
                
                window.update()
                time.sleep(0.4)
        dice_btn1['bg'] = '#777' 
        dice_btn2['bg'] = '#f00' 
        # dice_btn2.place(x=1345,y=30)

        # window.update()
        # time.sleep(4)
# ______________________________________________________________________________________

    def role2_2() :
        # frm_player_red.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_red.append(num)
        num_of_case = 0
        for i in count_red :
            num_of_case += i 
            window.update()
            time.sleep(0.1)
            
        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_red.place(x=x+10,y=y+10)
                winsound.Beep(500, 100)
                window.update()
                time.sleep(0.4)
                
        else:
            for j in range(num_of_case-num,num_of_case) :
                # winsound.Beep(500, 100)
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777') :
                    frm_player_red.place(x=130,y=55)
                    frm_first_player['bg'] = '#f00'
                    lbl_first_player['bg'] = '#f00'
                    frm_second_player['bg'] = '#0f0'
                    lbl_second_player['bg'] = '#0f0'
                    
                    winsound.Beep(50, 1000)
                    dice_btn2.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] == '#0f0') :
                    frm_player_red.place(x=130,y=55)
                    dice_btn2.place_forget()
                else :
                    frm_player_red.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
                
        dice_btn2['bg'] = '#777' 
        dice_btn1['bg'] = '#0f0' 
        # dice_btn2.place_forget()
        # dice_btn1.place(x=1345,y=30)


    # Button to move
    dice_btn1 = Button(master=frm_footer,text='Move green',font=('Arial',15),height=2,width=9,cursor='hand2',command=role2_1,bg='#0f0',fg='#fff')
    dice_btn1.place(x=1320,y=4)
    dice_btn2 = Button(master=frm_footer,text='Move red',font=('Arial',15),height=2,width=9,cursor='hand2',command=role2_2,bg='#f00',fg='#fff')
    dice_btn2.place(x=1200,y=4)
























def players3():
    sumfuns()
    numOfPlayer = 3
    # ______________________________________________/header\___________________________________________________


    # ______________________________________________/main\___________________________________________________
        # careau player
    frm_player_green = Frame(frm_main,height=20,width=20,bg='#0f0',highlightthickness=2,highlightbackground='#000')
    frm_player_green.place(x=1390,y=58)
    frm_player_red = Frame(frm_main,height=20,width=20,bg='#f00',highlightthickness=2,highlightbackground='#000')
    frm_player_red.place(x=1415,y=58)
    frm_player_blue = Frame(frm_main,height=20,width=20,bg='#00f',highlightthickness=2,highlightbackground='#000')
    frm_player_blue.place(x=1440,y=58)
        # order place
    frm_first_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_first_player.place(x=10, y=30)
    a = frm_first_player['bg']
    lbl_first_player = Label(frm_first_player,text='1',font=('Arial',20),bg=a)
    lbl_first_player.place(x=10,y=2)

    frm_second_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_second_player.place(x=10, y=100)
    b = frm_second_player['bg']
    lbl_second_player = Label(frm_second_player,text='2',font=('Arial',20),bg=b)
    lbl_second_player.place(x=10,y=2)

    frm_third_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_third_player.place(x=10, y=170)
    c = frm_third_player['bg']
    lbl_third_player = Label(frm_third_player,text='3',font=('Arial',20),bg=c)
    lbl_third_player.place(x=10,y=2)
    # ______________________________________________/footer\___________________________________________________
        # Display result
    lbl_result = Label(frm_header,text='1...6',font=('Arial',25),height=3,width=15,relief="flat",bg='#000',fg='#fff',highlightthickness=4,highlightbackground='#fff')
    lbl_result.place(x=600,y=0)


    global count_green
    count_green = [100]
    global count_red
    count_red = [100]
    global count_blue
    count_blue = [100]


    def role3_1() :
        
        # Tritement du Role :
        # frm_player_green.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_green.append(num)
        frm_player_green['height'] = 30
        frm_player_green['width'] = 30
        num_of_case = 0
        for i in count_green :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_green.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        else:
            for j in range(num_of_case-num,num_of_case) :
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777'):
                    frm_player_green['height'] = 20
                    frm_player_green['width'] = 20
                    frm_player_green.place(x=85,y=60)
                    frm_first_player['bg'] = '#0f0'
                    lbl_first_player['bg'] = '#0f0'
                    dice_btn1.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] == '#777') :
                    frm_player_green['height'] = 20
                    frm_player_green['width'] = 20
                    frm_player_green.place(x=112,y=60)
                    frm_second_player['bg'] = '#0f0'
                    lbl_second_player['bg'] = '#0f0'
                    dice_btn1.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') :
                    frm_player_green['height'] = 20
                    frm_player_green['width'] = 20
                    frm_player_green.place(x=140,y=60)
                    frm_third_player['bg'] = '#0f0'
                    lbl_third_player['bg'] = '#0f0'
                    dice_btn1.place_forget()

                else :
                    frm_player_green.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)                
        dice_btn1['bg'] = '#777'
        dice_btn2['bg'] = '#f00'
        dice_btn3['bg'] = '#777'

        # window.update()
        # time.sleep(4)
# ______________________________________________________________________________________

    def role3_2() :
        # frm_player_red.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_red.append(num)
        frm_player_red['height'] = 30
        frm_player_red['width'] = 30
        num_of_case = 0
        for i in count_red :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_red.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        else:
            for j in range(num_of_case-num,num_of_case) :
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777') :
                    frm_player_red['height'] = 20
                    frm_player_red['width'] = 20
                    frm_player_red.place(x=85,y=60)
                    frm_first_player['bg'] = '#f00'
                    lbl_first_player['bg'] = '#f00'
                    dice_btn2.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] == '#777') :
                    frm_player_red['height'] = 20
                    frm_player_red['width'] = 20
                    frm_player_red.place(x=112,y=60)
                    frm_second_player['bg'] = '#f00'
                    lbl_second_player['bg'] = '#f00'
                    dice_btn2.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') :
                    frm_player_red['height'] = 20
                    frm_player_red['width'] = 20
                    frm_player_red.place(x=140,y=60)
                    frm_third_player['bg'] = '#f00'
                    lbl_third_player['bg'] = '#f00'
                    dice_btn2.place_forget()
                else :
                    frm_player_red.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        dice_btn1['bg'] = '#777'
        dice_btn2['bg'] = '#777'
        dice_btn3['bg'] = '#00f'
        
        # dice_btn2.place_forget()
        # dice_btn1.place(x=1345,y=30)


# ______________________________________________________________________________________

    def role3_3() :
        # frm_player_blue.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_blue.append(num)
        frm_player_blue['height'] = 30
        frm_player_blue['width'] = 30
        num_of_case = 0
        for i in count_blue :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_blue.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        else:
            for j in range(num_of_case-num,num_of_case) :
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777') :
                    frm_player_blue['height'] = 20
                    frm_player_blue['width'] = 20
                    frm_player_blue.place(x=85,y=60)
                    frm_first_player['bg'] = '#00f'
                    lbl_first_player['bg'] = '#00f'
                    dice_btn3.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] == '#777') :
                    frm_player_blue['height'] = 20
                    frm_player_blue['width'] = 20
                    frm_player_blue.place(x=112,y=60)
                    frm_second_player['bg'] = '#00f'
                    lbl_second_player['bg'] = '#00f'
                    dice_btn3.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') :
                    frm_player_blue['height'] = 20
                    frm_player_blue['width'] = 20
                    frm_player_blue.place(x=140,y=60)
                    frm_third_player['bg'] = '#00f'
                    lbl_third_player['bg'] = '#00f'
                    dice_btn3.place_forget()
                else :
                    frm_player_blue.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        dice_btn1['bg'] = '#0f0'
        dice_btn2['bg'] = '#777'
        dice_btn3['bg'] = '#777'
        
        # dice_btn2.place_forget()
        # dice_btn1.place(x=1345,y=30)


    # Button to move
    dice_btn1 = Button(master=frm_footer,text='Move green',font=('Arial',15),height=2,width=9,cursor='hand2',command=role3_1,bg='#0f0',fg='#fff')
    dice_btn1.place(x=1345,y=4)
    dice_btn2 = Button(master=frm_footer,text='Move red',font=('Arial',15),height=2,width=9,cursor='hand2',command=role3_2,bg='#f00',fg='#fff')
    dice_btn2.place(x=1345,y=70)
    dice_btn3 = Button(master=frm_footer,text='Move blue',font=('Arial',15),height=2,width=9,cursor='hand2',command=role3_3,bg='#00f',fg='#fff')
    dice_btn3.place(x=1235,y=35)



























def players4():
    sumfuns()
    numOfPlayer = 4
    # ______________________________________________/header\___________________________________________________


    # ______________________________________________/main\___________________________________________________
        # careau player
    frm_player_green = Frame(frm_main,height=20,width=20,bg='#0f0',highlightthickness=2,highlightbackground='#000')
    frm_player_green.place(x=1385,y=58)
    frm_player_red = Frame(frm_main,height=20,width=20,bg='#f00',highlightthickness=2,highlightbackground='#000')
    frm_player_red.place(x=1405,y=58)
    frm_player_blue = Frame(frm_main,height=20,width=20,bg='#00f',highlightthickness=2,highlightbackground='#000')
    frm_player_blue.place(x=1425,y=58)
    frm_player_yellow = Frame(frm_main,height=20,width=20,bg='#ff0',highlightthickness=2,highlightbackground='#000')
    frm_player_yellow.place(x=1445,y=58)

        # order place
    frm_first_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_first_player.place(x=10, y=30)
    a = frm_first_player['bg']
    lbl_first_player = Label(frm_first_player,text='1',font=('Arial',20),bg=a)
    lbl_first_player.place(x=10,y=2)

    frm_second_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_second_player.place(x=10, y=100)
    b = frm_second_player['bg']
    lbl_second_player = Label(frm_second_player,text='2',font=('Arial',20),bg=b)
    lbl_second_player.place(x=10,y=2)

    frm_third_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_third_player.place(x=10, y=170)
    c = frm_third_player['bg']
    lbl_third_player = Label(frm_third_player,text='3',font=('Arial',20),bg=c)
    lbl_third_player.place(x=10,y=2)

    frm_fourth_player = Frame(frm_final_place, height=50, width=50, bg='#777',highlightthickness=4,highlightbackground='#000')
    frm_fourth_player.place(x=10, y=240)
    d = frm_fourth_player['bg']
    lbl_fourth_player = Label(frm_fourth_player,text='4',font=('Arial',20),bg=d)
    lbl_fourth_player.place(x=10,y=2)
    # ______________________________________________/footer\___________________________________________________
        # Display result
    lbl_result = Label(frm_header,text='1...6',font=('Arial',25),height=3,width=15,relief="flat",bg='#000',fg='#fff',highlightthickness=4,highlightbackground='#fff')
    lbl_result.place(x=600,y=0)


    global count_green
    count_green = [120]
    global count_red
    count_red = [120]
    global count_blue
    count_blue = [120]
    global count_yellow
    count_yellow = [120]


    def role4_1() :
        
        # Tritement du Role :
        # frm_player_green.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_green.append(num)
        frm_player_green['height'] = 30
        frm_player_green['width'] = 30
        num_of_case = 0
        for i in count_green :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_green.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        else:
            for j in range(num_of_case-num,num_of_case) :
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777'):
                    frm_player_green['height'] = 20
                    frm_player_green['width'] = 20
                    frm_player_green.place(x=80,y=60)
                    frm_first_player['bg'] = '#0f0'
                    lbl_first_player['bg'] = '#0f0'
                    dice_btn1.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] == '#777') :
                    frm_player_green['height'] = 20
                    frm_player_green['width'] = 20
                    frm_player_green.place(x=100,y=60)
                    frm_second_player['bg'] = '#0f0'
                    lbl_second_player['bg'] = '#0f0'
                    dice_btn1.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777' and (frm_third_player['bg'] == '#777')) :
                    frm_player_green['height'] = 20
                    frm_player_green['width'] = 20
                    frm_player_green.place(x=130,y=60)
                    frm_third_player['bg'] = '#0f0'
                    lbl_third_player['bg'] = '#0f0'
                    dice_btn1.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') and (frm_third_player['bg'] != '#777') :
                    frm_player_green['height'] = 20
                    frm_player_green['width'] = 20
                    frm_player_green.place(x=150,y=60)
                    frm_fourth_player['bg'] = '#0f0'
                    lbl_fourth_player['bg'] = '#0f0'
                    dice_btn1.place_forget()

                else :
                    frm_player_green.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)                
        dice_btn1['bg'] = '#777'
        dice_btn2['bg'] = '#f00'
        dice_btn3['bg'] = '#777'
        dice_btn4['bg'] = '#777'

        # window.update()
        # time.sleep(4)
# ______________________________________________________________________________________

    def role4_2() :
        # frm_player_red.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_red.append(num)
        frm_player_red['height'] = 30
        frm_player_red['width'] = 30
        num_of_case = 0
        for i in count_red :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_red.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        else:
            for j in range(num_of_case-num,num_of_case) :
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777') :
                    frm_player_red['height'] = 20
                    frm_player_red['width'] = 20
                    frm_player_red.place(x=80,y=60)
                    frm_first_player['bg'] = '#f00'
                    lbl_first_player['bg'] = '#f00'
                    dice_btn2.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] == '#777') :
                    frm_player_red['height'] = 20
                    frm_player_red['width'] = 20
                    frm_player_red.place(x=100,y=60)
                    frm_second_player['bg'] = '#f00'
                    lbl_second_player['bg'] = '#f00'
                    dice_btn2.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777' and (frm_third_player['bg'] == '#777')) :
                    frm_player_red['height'] = 20
                    frm_player_red['width'] = 20
                    frm_player_red.place(x=130,y=60)
                    frm_third_player['bg'] = '#f00'
                    lbl_third_player['bg'] = '#f00'
                    dice_btn2.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') and (frm_third_player['bg'] != '#777') :
                    frm_player_red['height'] = 20
                    frm_player_red['width'] = 20
                    frm_player_red.place(x=150,y=60)
                    frm_fourth_player['bg'] = '#f00'
                    lbl_fourth_player['bg'] = '#f00'
                    dice_btn2.place_forget()
                else :
                    frm_player_red.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        dice_btn1['bg'] = '#777'
        dice_btn2['bg'] = '#777'
        dice_btn3['bg'] = '#00f'
        dice_btn4['bg'] = '#777'
        
        # dice_btn2.place_forget()
        # dice_btn1.place(x=1345,y=30)


# ______________________________________________________________________________________

    def role4_3() :
        # frm_player_blue.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_blue.append(num)
        frm_player_blue['height'] = 30
        frm_player_blue['width'] = 30
        num_of_case = 0
        for i in count_blue :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_blue.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        else:
            for j in range(num_of_case-num,num_of_case) :
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777') :
                    frm_player_blue['height'] = 20
                    frm_player_blue['width'] = 20
                    frm_player_blue.place(x=80,y=60)
                    frm_first_player['bg'] = '#00f'
                    lbl_first_player['bg'] = '#00f'
                    dice_btn3.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] == '#777') :
                    frm_player_blue['height'] = 20
                    frm_player_blue['width'] = 20
                    frm_player_blue.place(x=100,y=60)
                    frm_second_player['bg'] = '#00f'
                    lbl_second_player['bg'] = '#00f'
                    dice_btn3.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') and (frm_third_player['bg'] == '#777') :
                    frm_player_blue['height'] = 20
                    frm_player_blue['width'] = 20
                    frm_player_blue.place(x=130,y=60)
                    frm_third_player['bg'] = '#00f'
                    lbl_third_player['bg'] = '#00f'
                    dice_btn3.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') and (frm_third_player['bg'] != '#777') :
                    frm_player_blue['height'] = 20
                    frm_player_blue['width'] = 20
                    frm_player_blue.place(x=150,y=60)
                    frm_fourth_player['bg'] = '#00f'
                    lbl_fourth_player['bg'] = '#00f'
                    dice_btn3.place_forget()
                else :
                    frm_player_blue.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        dice_btn1['bg'] = '#777'
        dice_btn2['bg'] = '#777'
        dice_btn3['bg'] = '#777'
        dice_btn4['bg'] = '#ff0'



# ______________________________________________________________________________________

    def role4_4() :
        # frm_player_blue.place_forget()
        a = random.randint(1, 6)
        num = a
        lbl_result['text'] = str(num)
        count_yellow.append(num)
        frm_player_yellow['height'] = 30
        frm_player_yellow['width'] = 30
        num_of_case = 0
        for i in count_yellow :
            num_of_case += i 

        if num_of_case == num :
            for i in range(num) :
                x = tab_of_cordonne[i][0]
                y = tab_of_cordonne[i][1]
                frm_player_yellow.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        else:
            for j in range(num_of_case-num,num_of_case) :
                x = tab_of_cordonne[j][0]
                y = tab_of_cordonne[j][1]
                if (x == 80 and y == 55) and (frm_first_player['bg'] == '#777') :
                    frm_player_yellow['height'] = 20
                    frm_player_yellow['width'] = 20
                    frm_player_yellow.place(x=80,y=60)
                    frm_first_player['bg'] = '#ff0'
                    lbl_first_player['bg'] = '#ff0'
                    dice_btn4.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] == '#777') :
                    frm_player_yellow['height'] = 20
                    frm_player_yellow['width'] = 20
                    frm_player_yellow.place(x=100,y=60)
                    frm_second_player['bg'] = '#ff0'
                    lbl_second_player['bg'] = '#ff0'
                    dice_btn4.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') and (frm_third_player['bg'] == '#777') :
                    frm_player_yellow['height'] = 20
                    frm_player_yellow['width'] = 20
                    frm_player_yellow.place(x=130,y=60)
                    frm_third_player['bg'] = '#ff0'
                    lbl_third_player['bg'] = '#ff0'
                    dice_btn4.place_forget()
                elif (x == 80 and y == 55) and (frm_first_player['bg'] != '#777') and (frm_second_player['bg'] != '#777') and (frm_third_player['bg'] != '#777') :
                    frm_player_yellow['height'] = 20
                    frm_player_yellow['width'] = 20
                    frm_player_yellow.place(x=150,y=60)
                    frm_fourth_player['bg'] = '#ff0'
                    lbl_fourth_player['bg'] = '#ff0'
                    dice_btn4.place_forget()
                else :
                    frm_player_yellow.place(x=x+10,y=y+10)
                window.update()
                time.sleep(0.4)
        dice_btn1['bg'] = '#0f0'
        dice_btn2['bg'] = '#777'
        dice_btn3['bg'] = '#777'
        dice_btn4['bg'] = '#777'
        
        # dice_btn2.place_forget()
        # dice_btn1.place(x=1345,y=30)


    # Button to move
    dice_btn1 = Button(master=frm_footer,text='Move green',font=('Arial',15),height=2,width=9,cursor='hand2',command=role4_1,bg='#0f0',fg='#000')
    dice_btn1.place(x=1345,y=4)
    dice_btn2 = Button(master=frm_footer,text='Move red',font=('Arial',15),height=2,width=9,cursor='hand2',command=role4_2,bg='#f00',fg='#000')
    dice_btn2.place(x=1345,y=70)
    dice_btn3 = Button(master=frm_footer,text='Move blue',font=('Arial',15),height=2,width=9,cursor='hand2',command=role4_3,bg='#00f',fg='#000')
    dice_btn3.place(x=1235,y=70)
    dice_btn4 = Button(master=frm_footer,text='Move yellow',font=('Arial',15),height=2,width=9,cursor='hand2',command=role4_4,bg='#ff0',fg='#000')
    dice_btn4.place(x=1235,y=4)





window = Tk()
window.title('Version 1.0')
window.geometry('550x350+500+200')
window.resizable(False, False)
window['bg'] = "#333"


lbl_select = Label(text='Select number of players :', font=('Arial', 30), bg='#333', fg='#fff')
lbl_select.place(x=45, y=80)


btn_player2 = customtkinter.CTkButton(master=window, text='2 Players',corner_radius=40, font=('Arial', 20), command=players2)
btn_player2.place(x=30, y=250)

btn_player3 = customtkinter.CTkButton(master=window, text='3 Players',corner_radius=40, font=('Arial', 20), command=players3)
btn_player3.place(x=200, y=250)

btn_player4 = customtkinter.CTkButton(master=window, text='4 Players',corner_radius=40, font=('Arial', 20), command=players4)
btn_player4.place(x=370, y=250)


window.mainloop()