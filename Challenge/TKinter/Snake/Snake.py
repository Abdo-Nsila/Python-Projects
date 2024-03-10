from playsound import playsound
from winsound import * 
from tkinter import *
import random
import time


class Plate() :
    frms = []
    cords = []
    x_object  = 0
    y_object = 0
    h=15
    w=15
    speed = 0.02
    def __init__(self,x_snake=0,y_snake=0,color_snake="#0a0",color_object="#b00"):
        self._x_snake = x_snake 
        self._y_snake = y_snake 
        self._color_snake = color_snake
        # --------------------------------- 
        self._color_object = color_object

 

class Snake(Plate) :

    def __init__(self, x_snake=0, y_snake=0, color_snake="#0a0",color_object="#b00"):
        super().__init__(x_snake, y_snake, color_snake,color_object)

    def respawn(self) :
        frm_snake = Frame(frm_game,height=Snake.h,width=Snake.w,bg=self._color_snake)
        frm_snake.place(x=self._x_snake,y=self._y_snake)
        Plate.frms.append(frm_snake)
        Plate.cords.append([self._x_snake,self._y_snake])

    def eat() :
        global lbl_r
        if (Snake.cords[0][0] == Object.x_object) and (Snake.cords[0][1] == Object.y_object) :
            lbl_r['text'] = str(int(lbl_r['text'])+1)
            add_more()
            obj.random_spawn()

    def move(self,a,b,pos) :
        while True :
            window.update()
            time.sleep(Plate.speed)
            # print(Snake.frms)
            # print(Snake.cords)
            for i in range(len(Snake.cords)-1,-1,-1) :
                Snake.eat()
                if i == 0 :
                    Snake.cords[i][0] += a
                    x = Snake.cords[i][0]
                    Snake.cords[i][1] += b
                    y = Snake.cords[i][1]
                    Snake.frms[i].place(x=x,y=y)
                else :
                    Snake.cords[i][0] = Snake.cords[i-1][0]
                    Snake.cords[i][1] = Snake.cords[i-1][1]
                    x = Snake.cords[i][0]
                    y = Snake.cords[i][1]
                    Snake.frms[i].place(x=x,y=y)
            check_collision()
            if pos == "r" :
                if Snake.cords[0][0] > 1305 :
                    Snake.cords[0][0] = 0
            elif pos == "l" :
                if Snake.cords[0][0] < 0 :
                    Snake.cords[0][0] = 1305
            elif pos == "u" :
                if Snake.cords[0][1] < 0 :
                    Snake.cords[0][1] = 645
            elif pos == "d" :
                if Snake.cords[0][1] > 645 :
                    Snake.cords[0][1] = 0





class Object(Plate) :

    def __init__(self, x_snake=0, y_snake=0, color_snake="#0a0",color_object="#b00"):
        super().__init__(x_snake, y_snake, color_snake,color_object)

    def respawn(self) :
        global frm_object
        frm_object = Frame(frm_game,height=Snake.h,width=Snake.w,bg=self._color_object,highlightbackground="#000",highlightthickness=3)
        Object.x_object = random.randrange(0,1305,Snake.h)
        a = Object.x_object 
        Object.y_object = random.randrange(0,645,Snake.h)
        b = Object.y_object
        frm_object.place(x=a,y=b)

    def random_spawn(self) :
        Object.x_object = random.randrange(0,1305,Snake.h)
        Object.y_object = random.randrange(0,645,Snake.h)
        frm_object.place(x=Object.x_object,y=Object.y_object)



        

snk = Snake()
obj = Object()

def game_over() :
    frm_header.pack_forget()
    frm_game.pack_forget()
    frm_lost = Frame(window,height=800,width=1300,bg="#222")
    frm_lost.pack()
    lbl_over = Label(text="Game Over",font=('Aril',70),fg='#f00',bg='#222')
    lbl_over.place(x=400,y=350)

def check_collision() :
    for i in range(1,len(Snake.cords)) :
        if (Snake.cords[0][0] == Snake.cords[i][0]) and (Snake.cords[0][1] == Snake.cords[i][1]) :
            game_over()
    if (Snake.cords[0][0] < 0) or (Snake.cords[0][0] == 1305) or (Snake.cords[0][1] < 0) or (Snake.cords[0][1] == 645) :
        game_over()

def add_more() :
    add_frm = Frame(frm_game,height=Snake.h,width=Snake.w,bg="#0a0",highlightbackground="#000",highlightthickness=2)
    Snake.frms.append(add_frm)
    Snake.cords.append([0,0])

def add(x=0) :
    global frm_game
    for i in range(x) :
        add_more()


role = 2
def right(event) :
    global role
    if role != 0 :
        role = 0
        snk.move(Snake.h,0,"r")
    
def left(event) :
    global role
    if role != 0 :
        role = 0
        snk.move(-(Snake.h),0,"l")

def up(event) :
    global role
    if role != 1 :
        role = 1
        snk.move(0,-(Snake.h),"u")

def down(event) :
    global role
    if role != 1 :
        role = 1
        snk.move(0,Snake.h,"d")

    
window = Tk()
window.geometry("1305x800+110+15")
window.title("SNAKE")
window.bind("<Right>",right)
window.bind("<Left>",left)
window.bind("<Up>",up)
window.bind("<Down>",down)

frm_header = Frame(window,height="155",width="1305",bg="#ccc")
frm_header.pack()
lbl_score = Label(text="Score : ",font=('Arial',60),bg="#ccc")
lbl_score.place(x=550,y=25)
lbl_r = Label(text="0",font=('Arial',60),bg="#ccc")
lbl_r.place(x=830,y=25)
# --------------------------------------------------------------------
frm_game = Frame(window,height="645",width="1305",bg="#0fb")
frm_game.pack()

snk.respawn()
obj.respawn()
add()

window.mainloop()
