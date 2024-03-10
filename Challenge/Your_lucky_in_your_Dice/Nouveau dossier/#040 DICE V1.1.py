from tkinter import *
import random
import time
from PIL import Image, ImageTk

turn = 0
# ['red', 'blue', 'green', 'yellow']
tab_c_time = [-1, -1, -1, -1]


def forget_page1():
    # clear
    lbl_select.place_forget()
    btn_player2.place_forget()
    btn_player3.place_forget()
    btn_player4.place_forget()

# game page
# steps
'''in stable_designe() you will found most frame in page of game that doesn't change (stable) include steps 1-108'''
def stable_designe(tab_of_players):
    # style new window
    global frm_header, tab_of_cordonne, frm_footer, frm_main, dice_lbl, finl_step,tab_up,tab_down,message_lbl

    window.geometry('1350x680+10+15')

    # header
    frm_header = Frame(width=1340, height=100, bg='#3B3B3B')
    frm_header.place(x=5, y=0)
    # players coulor
    for i in range(len(tab_of_players)):
        header_frm_color = Canvas(frm_header, width=30, height=30, background=tab_of_players[i])
        header_frm_color.place(x=40+i*100, y=15)
        header_lbl_color = Label(frm_header, text='Player '+str(i+1),bg='#aaa', fg='#222', font=('Arial', 15))
        header_lbl_color.place(x=17+i*100, y=50)

    # main
    frm_main = Frame(width=1340, height=480, bg='#555')
    frm_main.place(x=5, y=105)
    # steps
    lbl_start = Label(frm_main, text='Start', font=('Arial', 20),fg='#555', width=5, highlightbackground="#555", highlightthickness=1)
    lbl_start.place(x=1250, y=2)

    first_step = Frame(frm_main, height=35, width=90, bg='#fff',highlightbackground="#555", highlightthickness=1)
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
    # for reverse the colom not order (for make steps in right order) 
    for i in range(9, len(tab_of_cordonne), 18):
        trev = []
        for j in range(i, i+8):
            trev.append(tab_of_cordonne[j])
        trev.reverse()
        for q in range(len(trev)):
            tab_of_cordonne[i+q] = trev[q]

    # place my steps with designe and number it (using cordonne)
    for q in range(len(tab_of_cordonne)):
        all_steps = Frame(frm_main, height=50, width=50, bg='#fff',highlightbackground="#666", highlightthickness=1)
        all_steps.place(x=tab_of_cordonne[q][0], y=tab_of_cordonne[q][1])
        oreder_steps = Label(all_steps, text=str(f"{(q+1):03}"), fg='#bbb', bg='#fff')
        oreder_steps.place(x=11, y=15)

    finl_step = Frame(frm_main, height=92, width=30, bg='#fff',highlightbackground="#555", highlightthickness=1)
    finl_step.place(x=86, y=54)

    lbl_end =Canvas(frm_main, width = 30, height = 80)
    lbl_end.place(x=50, y=58)
    lbl_end.create_text(14, 65, text = "End",fill='#555',font=('Arial', 20), angle = 90, anchor = "w")

    tab_up = (20,40,50,60,70,80)
    tab_down = (10,27,47,57,77,87,94,101)
    for i in range(len(tab_up)):
        up_frm = Frame(frm_main, height=50, width=50, bg='#496149',highlightbackground="#666", highlightthickness=1)
        up_frm.place(x=tab_of_cordonne[tab_up[i]][0], y=tab_of_cordonne[tab_up[i]][1])
        num_up= Label(up_frm, text='+ 5', fg='#fff', bg='#496149')
        num_up.place(x=11, y=15)
    for i in range(len(tab_down)):
        down_frm = Frame(frm_main, height=50, width=50, bg='#BA8570',highlightbackground="#666", highlightthickness=1)
        down_frm.place(x=tab_of_cordonne[tab_down[i]][0], y=tab_of_cordonne[tab_down[i]][1])
        num_down= Label(down_frm, text='- 5', fg='#fff', bg='#BA8570')
        num_down.place(x=11, y=15)
    start_eat_frm = Frame(frm_main, height=50, width=50, bg='#81A18A',highlightbackground="#666", highlightthickness=1)
    start_eat_frm.place(x=tab_of_cordonne[11][0], y=tab_of_cordonne[11][1])
    start_eat_lbl= Label(start_eat_frm, text='Eat', fg='#fff', bg='#81A18A')
    start_eat_lbl.place(x=11, y=15)
    # footer
    frm_footer = Frame(width=1340, height=85, bg='#3B3B3B')
    frm_footer.place(x=5, y=590)
    # this label for put the random number of dice I put it here for make it easy to use in next functions
    dice_lbl = Label(frm_footer, text='',bg= '#3B3B3B',fg='#fff', font=('Arial', 30))
    message_lbl = Label(frm_footer, text='',bg= '#3B3B3B',fg='#fff',font=('Arial', 30))


# ------------------------------------------
# variable Designe
'''#set default postions of player in start frame'''


def set_default_position(tab_of_players):
    global t_positions
    tab = [['red_position' ,'#a00'] ,['blue_position','#00a'] ,['green_position','#0a0'] ,['yellow_position','#aa0'] ]
    t_positions = []
    for i in range(len(tab_of_players)):
        locals()[tab[i][0]] = Canvas(frm_main, width=20, height=20, background=tab[i][1])
        locals()[tab[i][0]].place(x=1246+i*22, y=46)
        t_positions.append(locals()[tab[i][0]])

'''##Set the turn of who'''

turnWho = -1
def turn_of_who(tab_coordones_time,tab_of_players):
    global turnWho
    turnWho += 1
    if turnWho > len(tab_of_players)-1:
        turnWho = 0
    if tab_coordones_time[turnWho] == 'done':
        turn_of_who(tab_coordones_time,tab_of_players)
        return
    color_turn = Canvas(frm_header, width=30, height=30, background=tab_of_players[turnWho])
    color_turn.place(x=1277, y=35)

'''#move player frm last postion (prevPos) to next position (futurePos) after click on dice'''

def sleep_s():
    time.sleep(0.1)
    window.update()

def move_step_by_step(color, prevPos, futurePos,pas):
    fuPos = prevPos+futurePos+1
    if fuPos > 108:
        fuPos = 108
    for i in range(prevPos+1, fuPos,pas):
        # print(i)
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
    dice_icon = PhotoImage(file='dice.png')
    window1.iconphoto(False, dice_icon)
    lbl_winers = Label(text=' - '.join(tab).upper()).pack()
    win_frm = Canvas(width=30, height=30, background=tab[0])
    win_frm.place(x=257, y=100)
    if len(tab) > 1:
        if len(tab) == 2:
            win_frm1 = Canvas(width=30, height=30, background=tab[1])
            win_frm1.place(x=257, y=135)
        else:
            win_frm1 = Canvas(width=30, height=30, background=tab[1])
            win_frm1.place(x=225, y=132)
            win_frm2 = Canvas(width=30, height=30, background=tab[2])
            win_frm2.place(x=289, y=132)
    lbl_winer = Label(
        text='The '+tab[0].upper()+' is The King  \/\/ | |\|').place(x=170, y=250)
    exit_bnt = Button(text='Exit',command=lambda:window1.destroy()).place(x = 245,y=300)

    window1.mainloop()
###############################################

# dice function controle moving of every player
'''lucky and unlucky steps (this funtions here it's the deep of all my code i think)'''
def emoji(state):
        tab_emoji_happy = ['\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/','(¬‿¬)','ヾ(⌐■_■)ノ♪','~(˘▾˘~)','ᕦ(ò_óˇ)ᕤ','(▀̿Ĺ̯▀̿ ̿)']
        tab_emoji_cry = ['(;´༎ຶД༎ຶ`)','(๑òᗜó)','ب_ب','╥﹏╥','(TдT)','┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻']
        tab_emoji_laugh = ['(ᗒ ᗨᗕ)','(๑òᗜó)','( ՞ਊ՞)','( ͡⚆ ͜ʖ ͡⚆)','ᕦ(ò_óˇ)ᕤ','☼.☼']
        rand = random.randint(0,5)
        message_lbl['text'] = locals()['tab_emoji_'+state][rand]

def to_up(index_of):
    global tab_c_time
    if tab_c_time[index_of] in tab_up:
        time.sleep(0.5)
        move_step_by_step(t_positions[index_of], tab_c_time[index_of]-1, +6,+1)
        tab_c_time[index_of] += 5
        emoji('happy')
        on_other_player(index_of)
def to_down(index_of):
    global tab_c_time
    if tab_c_time[index_of] in tab_down:
        time.sleep(0.5)
        move_step_by_step(t_positions[index_of], tab_c_time[index_of]-1, -6,-1)
        tab_c_time[index_of] -= 5
        emoji('cry')
        on_other_player(index_of)
def on_other_player(index_of):
    global tab_c_time
    tab_c_time_other = tab_c_time.copy()
    tab_c_time_other[index_of] = 'turn'
    if   tab_c_time[index_of] > 11 and tab_c_time[index_of] in tab_c_time_other:
        myindex = tab_c_time_other.index(tab_c_time[index_of])
        time.sleep(0.5)
        move_step_by_step(t_positions[myindex], tab_c_time[myindex]-1, -4,-1)
        tab_c_time[myindex]-=3
        emoji('laugh')
        to_up(myindex)
        to_down(myindex)
        on_other_player(myindex)
        

'''***********************'''

order_of_wins = []
def move_position(dice_random_number,myButton):
    global tab_of_players, turn, finl_step,tab_c_time,tab_c_time_other
    # turn_of_who(tab_c_time)
    '''this condition here for stop game when get all winers'''
    if tab_c_time.count('done') > (len(tab_of_players)/2) or (tab_c_time.count('done') == 1 and len(tab_of_players) == 2):
        # print(order_of_wins)
        window.destroy()
        win_players_page(order_of_wins)
        return
    # print('turn is : ',turn)
    # t_done_positions = [[56],[78],[100],[122]]
    #'''for skip player that done or win'''
    if tab_c_time[turn] == 'done':
        if turn == 3:
            turn = 0
        else:
            turn += 1
        move_position(dice_random_number,myButton)
        return
    #'''for last move before done or win '''
    elif (tab_c_time[turn]+dice_random_number) >= len(tab_of_cordonne):
        numOfdone = len(tab_of_cordonne)-tab_c_time[turn] - 1
        move_step_by_step(t_positions[turn], tab_c_time[turn], numOfdone,1)
        sleep_s()
        t_positions[turn].place(x=90, y=56+turn*22)
        tab_c_time[turn] = 'done'
        emoji('laugh')
        order_of_wins.append(tab_of_players[turn])
    #'''move player by calcul last play + dice_number and move it step by step when call "move_step_by_step()" Funtion '''
    else:
        move_step_by_step(t_positions[turn], tab_c_time[turn], dice_random_number,1)
        tab_c_time[turn] += dice_random_number

    # print(tab_of_players)
    # print(tab_c_time)

    '''luck unluchy place'''
    
    tab_c_time_other = tab_c_time.copy()
    tab_c_time_other[turn] = 'turn'
    to_up(turn)
    to_down(turn)
    if not(tab_c_time[turn] == 'done'):
        on_other_player(turn)
    '''------------------'''


    turn_of_who(tab_c_time,tab_of_players)
    
    #active dice button
    # time.sleep(5)
    myButton.config(state = 'active')

def move_player(myButton):
    global turn, dice_random_number, image,btn_frm
    #disable dice button
    myButton.config(state = 'disabled')
    
    dice_random_number = random.randint(1, 6)
    dice_lbl['text'] = str(dice_random_number)
    
    move_position(dice_random_number,myButton)
    turn += 1
    if turn > len(tab_of_players)-1:
        turn = 0
    

def var_design(tab_of_players):
    turn_of_who([-1, -1, -1, -1],tab_of_players)
    dice_bnt = Button(frm_footer, image=img, command=lambda:move_player(dice_bnt))
    dice_bnt.place(x=1255, y=13)
    dice_lbl.place(x=1210, y=17)
    message_lbl.place(x=50,y=17)
# ------------------------------------------

def sumfuns(tab):
    global tab_of_players
    tab_of_players = tab 
    forget_page1()
    stable_designe(tab_of_players)
    var_design(tab_of_players)
    set_default_position(tab_of_players)


'''this when every thing start, when user select number of player'''
window = Tk()
window.title('DICE V1.0')
window.geometry('550x350+500+200')
window.resizable(False, False)
window['bg'] = "#333"
dice_icon = PhotoImage(file='dice.png')
# Setting icon
window.iconphoto(False, dice_icon)

'''# Select number of players first page '''

lbl_select = Label(text='Select number of players :',font=('Arial', 30), bg='#333', fg='#fff')
lbl_select.place(x=45, y=80)


btn_player2 = Button(master=window, text='2 Players',font=('Arial', 20), command=lambda:sumfuns(['red', 'blue']))
btn_player2.place(x=30, y=250)

btn_player3 = Button(master=window, text='3 Players',font=('Arial', 20), command=lambda:sumfuns(['red', 'blue', 'green']))
btn_player3.place(x=200, y=250)
'''customtkinter.CTkButton'''
btn_player4 = Button(master=window, text='4 Players',font=('Arial', 20),command=lambda:sumfuns(['red', 'blue', 'green', 'yellow']))
btn_player4.place(x=370, y=250)

'''button of dice image import and edit'''
# import customtkinter
image = Image.open('dicee.png')
# Resize the Image
image = image.resize((55, 55))
# Convert the image to PhotoImage
img = ImageTk.PhotoImage(image)
# -------------------------------------------
window.mainloop()
# '''print'''