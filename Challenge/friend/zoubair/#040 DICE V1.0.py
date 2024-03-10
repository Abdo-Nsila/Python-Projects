import tkinter
from tkinter import *
import random
from tkinter import ttk
import time
# import customtkinter


turn = 0
red_x_y = -1
blue_x_y = -1
green_x_y = -1
yellow_x_y = -1


def forget_page1():
    # clear
    lbl_select.place_forget()
    btn_player2.place_forget()
    btn_player3.place_forget()
    btn_player4.place_forget()


# game page
# steps
'''in stable_designe funtion you found most frame in page of game that doesn't change (stable) include steps 1-108'''


def stable_designe(tab_of_players):
    # style new window
    global frm_header, tab_of_cordonne, frm_footer, frm_main, dice_lbl, finl_step

    window.geometry('1350x680+10+15')

    # header
    frm_header = Frame(width=1340, height=100, bg='#444')
    frm_header.place(x=5, y=0)
    # players coulor
    header_frm_red = Canvas(frm_header, width=30, height=30, background='#a00')
    header_frm_red.place(x=40, y=15)
    header_lbl_red = Label(frm_header, text='Player 1',
                            bg='#aaa', fg='#222', font=('Arial', 15))
    header_lbl_red.place(x=17, y=50)
    header_frm_blue = Canvas(frm_header, width=30,
                            height=30, background='#00a')
    header_frm_blue.place(x=130, y=15)
    # header_frm_blue.create_oval(300,360,310,310)
    header_lbl_blue = Label(frm_header, text='Player 2',
                            bg='#aaa', fg='#222', font=('Arial', 15))
    header_lbl_blue.place(x=107, y=50)
    if len(tab_of_players) > 2:
        header_frm_green = Canvas(
            frm_header, width=30, height=30, background='#0a0')
        header_frm_green.place(x=220, y=15)
        header_lbl_green = Label(
            frm_header, text='Player 3', bg='#aaa', fg='#222', font=('Arial', 15))
        header_lbl_green.place(x=197, y=50)
        if len(tab_of_players) > 3:
            header_frm_yellow = Canvas(
                frm_header, width=30, height=30, background='#aa0')
            header_frm_yellow.place(x=310, y=15)
            header_lbl_yellow = Label(
                frm_header, text='Player 4', bg='#aaa', fg='#222', font=('Arial', 15))
            header_lbl_yellow.place(x=287, y=50)

    # main
    frm_main = Frame(width=1340, height=480, bg='#555')
    frm_main.place(x=5, y=105)
    # steps
    lbl_start = Label(frm_main, text='Start', font=(
        'Arial', 20), width=5, highlightbackground="#000", highlightthickness=1)
    lbl_start.place(x=1250, y=2)

    first_step = Frame(frm_main, height=35, width=90, bg='#fff',
                        highlightbackground="#000", highlightthickness=1)
    first_step.place(x=1245, y=40)

    # make coordonnes of my steps
    tab_of_cordonne = []
    stepss = 0
    for i in range(23, 0, -2):
        stepss += 1
        for j in range(0, 8):
            tab_of_cordonne.append([118+(i*50), (j*50)+75])
        if stepss % 2 == 0:
            tab_of_cordonne.append([118+((i-1)*50), 75])
        else:
            tab_of_cordonne.append([118+((i-1)*50), 75+(7*50)])
    # for reverse the colom not order
    for i in range(9, len(tab_of_cordonne), 18):
        trev = []
        for j in range(i, i+8):
            trev.append(tab_of_cordonne[j])
        trev.reverse()
        for q in range(len(trev)):
            tab_of_cordonne[i+q] = trev[q]

    # place my steps designe (using cordonne)
    for q in range(len(tab_of_cordonne)):
        all_steps = Frame(frm_main, height=50, width=50, bg='#fff',
                          highlightbackground="#666", highlightthickness=1)
        all_steps.place(x=tab_of_cordonne[q][0], y=tab_of_cordonne[q][1])
        oreder_steps = Label(all_steps, text=str(
            f"{(q+1):03}"), fg='#bbb', bg='#fff')
        oreder_steps.place(x=11, y=15)
    # tab_of_cordonne.append([83,59])
    lbl_end = Label(frm_main, text='end', font=('Arial', 20), height=3, width=2,
                    highlightbackground="#000", highlightthickness=1, wraplength=1)
    lbl_end.place(x=46, y=49)

    finl_step = Frame(frm_main, height=92, width=30, bg='#fff',
                      highlightbackground="#000", highlightthickness=1)
    finl_step.place(x=86, y=54)

    # footer
    frm_footer = Frame(width=1340, height=85, bg='#444')
    frm_footer.place(x=5, y=590)
    # this label for put the number from dice I put it here for make it easy to use in next functions
    dice_lbl = Label(frm_footer, text='...', font=('Arial', 30))
    print(len(tab_of_cordonne))


# ------------------------------------------
# variable Designe
'''#set default postions of player in start frame'''


def set_default_position(tab_of_players):
    global red_position, blue_position, green_position, yellow_position
    red_position = Canvas(frm_main, width=20, height=20, background='#a00')
    red_position.place(x=1245+1, y=40+6)
    blue_position = Canvas(frm_main, width=20, height=20, background='#00a')
    blue_position.place(x=1245+20+3, y=40+6)
    if len(tab_of_players) > 2:
        green_position = Canvas(
            frm_main, width=20, height=20, background='#0a0')
        green_position.place(x=1245+40+5, y=40+6)
        if len(tab_of_players) > 3:
            yellow_position = Canvas(
                frm_main, width=20, height=20, background='#aa0')
            yellow_position.place(x=1245+60+7, y=40+6)


'''##Set the turn of who'''

turnWho = -1


def turn_of_who(t):
    global turnWho
    turnWho += 1
    if turnWho >= 4:
        turnWho = 0
    if t[turnWho] == 'done':
        turnWho += 1
    if turnWho >= 4:
        turnWho = 0
    red_turn = Canvas(frm_header, width=30, height=30, background='#a00')
    blue_turn = Canvas(frm_header, width=30, height=30, background='#00a')
    green_turn = Canvas(frm_header, width=30, height=30, background='#0a0')
    yellow_turn = Canvas(frm_header, width=30, height=30, background='#aa0')
    if turnWho == 0:
        red_turn.place(x=1200, y=50)
    elif turnWho == 1:
        blue_turn.place(x=1200, y=50)
    elif turnWho == 2:
        green_turn.place(x=1200, y=50)
    else:
        yellow_turn.place(x=1200, y=50)


'''#move player frm last postion (prevPos) to next position (futurePos) after click on dice'''


def sleep_s():
    time.sleep(0.4)
    window.update()


def move_step_by_step(color, prevPos, futurePos):
    fuPos = prevPos+futurePos+1
    if fuPos > 108:
        fuPos = 108
    for i in range(prevPos+1, fuPos):
        print(i)
        color.place(x=tab_of_cordonne[i][0]+15, y=tab_of_cordonne[i][1]+15)
        sleep_s()


##############################################
'''win_players_page funtion is for make page of winners player it's last page'''


def win_players_page(tab):
    window1 = Tk()
    window1.title('Congradilation V1.0')
    window1.geometry('550x350+500+200')
    window1.resizable(False, False)
    window1['bg'] = "#333"
    lbl_winers = Label(text=str(tab)).pack()
    window1.mainloop()
###############################################


# dice function controle moving of every player

order_of_wins = []


def move_position(dice_random_number):
    global red_x_y, blue_x_y, green_x_y, yellow_x_y, tab_of_players, turn, finl_step
    tab_c_time = [red_x_y, blue_x_y, green_x_y, yellow_x_y]
    # turn_of_who(tab_c_time)
    '''this condition here for stop game when get all winers'''
    if tab_c_time.count('done') > (len(tab_of_players)/2) or (tab_c_time.count('done') == 1 and len(tab_of_players) == 2):
        print(order_of_wins)
        window.destroy()
        win_players_page(order_of_wins)
        return

    print(len(tab_of_cordonne))
    # red
    '''there is 4 condition for every player [red,blue,green,yellow] i will explain on red and same thing for other players'''
    if turn == 0:

        #'''for skip player that done or win'''
        if red_x_y == 'done':
            turn += 1

        #'''for last move before done or win '''
        elif (red_x_y+dice_random_number) > len(tab_of_cordonne):
            numOfdone = len(tab_of_cordonne)-red_x_y - 1
            move_step_by_step(red_position, red_x_y, numOfdone)
            sleep_s()
            red_position.place(x=90, y=56)
            red_x_y = 'done'
            order_of_wins.append('red')
        #'''move player by calcul last play + dice_number and move it step by step when call "move_step_by_step()" Funtion '''
        else:
            move_step_by_step(red_position, red_x_y, dice_random_number)
            red_x_y += dice_random_number
    # blue
    if turn == 1:
        if blue_x_y == 'done':
            turn += 1

        elif (blue_x_y+dice_random_number) > len(tab_of_cordonne):
            numOfdone = len(tab_of_cordonne)-blue_x_y - 1
            move_step_by_step(blue_position, blue_x_y, numOfdone)
            sleep_s()
            blue_position.place(x=90, y=78)
            blue_x_y = 'done'
            order_of_wins.append('blue')
        else:
            move_step_by_step(blue_position, blue_x_y, dice_random_number)
            blue_x_y += dice_random_number

    # green
    if turn == 2:
        if green_x_y == 'done':
            turn += 1

        elif (green_x_y+dice_random_number) > len(tab_of_cordonne):
            numOfdone = len(tab_of_cordonne)-green_x_y - 1
            move_step_by_step(green_position, green_x_y, numOfdone)
            sleep_s()
            green_position.place(x=90, y=100)
            green_x_y = 'done'
            order_of_wins.append('green')
        else:
            move_step_by_step(green_position, green_x_y, dice_random_number)
            green_x_y += dice_random_number

    # yellow
    if turn == 3:
        if yellow_x_y == 'done':
            turn = 0
            move_position(dice_random_number)

        elif (yellow_x_y+dice_random_number) > len(tab_of_cordonne):
            numOfdone = len(tab_of_cordonne)-yellow_x_y - 1
            move_step_by_step(yellow_position, yellow_x_y, numOfdone)
            sleep_s()
            yellow_position.place(x=90, y=122)
            yellow_x_y = 'done'
            order_of_wins.append('yellow')
        else:
            move_step_by_step(yellow_position, yellow_x_y, dice_random_number)
            yellow_x_y += dice_random_number

    # remove player from tab_of_player (turn) afer get last place (win)
    tab_c_time = [red_x_y, blue_x_y, green_x_y, yellow_x_y]
    print(tab_of_players)
    print(tab_c_time)
    turn_of_who(tab_c_time)


def move_player():
    global turn, dice_random_number
    dice_random_number = random.randint(1, 6)
    dice_lbl['text'] = str(dice_random_number)

    move_position(dice_random_number)
    turn += 1
    if turn > len(tab_of_players)-1:
        turn = 0


def var_design(tab_of_players):
    turn_of_who([-1, -1, -1, -1])
    dice_bnt = Button(frm_footer, text='Move', background='#666', fg='#ccc', height=3,
                      highlightbackground="#ccc", highlightthickness=2, cursor='hand2', command=move_player)
    dice_bnt.place(x=1250, y=10)
    # dice_lbl = Label(frm_footer,text='...',font=('Arial',30))
    dice_lbl.place(x=1210, y=20)
# ------------------------------------------


def sumfuns(tab_of_players):
    forget_page1()
    stable_designe(tab_of_players)
    var_design(tab_of_players)
    set_default_position(tab_of_players)


def players2():

    global tab_of_players
    tab_of_players = ['red', 'blue']
    sumfuns(tab_of_players)


def players3():
    global tab_of_players
    tab_of_players = ['red', 'blue', 'green']
    sumfuns(tab_of_players)


def players4():
    global tab_of_players
    tab_of_players = ['red', 'blue', 'green', 'yellow']
    sumfuns(tab_of_players)


'''this when every thing start, when user select number of player'''
window = Tk()
window.title('DICE V1.0')
window.geometry('550x350+500+200')
window.resizable(False, False)
window['bg'] = "#333"

'''# Select number of players first page '''

lbl_select = Label(text='Select number of players :',
                   font=('Arial', 30), bg='#333', fg='#fff')
lbl_select.place(x=45, y=80)


btn_player2 = Button(master=window, text='2 Players',
                     font=('Arial', 20), command=players2)
btn_player2.place(x=30, y=250)

btn_player3 = Button(master=window, text='3 Players',
                     font=('Arial', 20), command=players3)
btn_player3.place(x=200, y=250)
'''customtkinter.CTkButton'''
btn_player4 = Button(master=window, text='4 Players',
                     font=('Arial', 20), command=players4)
btn_player4.place(x=370, y=250)

# -------------------------------------------

window.mainloop()
