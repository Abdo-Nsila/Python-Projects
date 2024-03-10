


# menubar = Menu(window)
# f = Menu(menubar ,tearoff=0)
# f.add_command(label='Play')
# f.add_separator()
# f.add_command(label='Restart')
# f.add_separator()
# f.add_command(label='Score')
# f.add_separator()
# f.add_command(label='Player')
# f.add_separator()
# f.add_command(label='Exit',command=window.quit)
# menubar.add_cascade(label='Game',menu=f)
# window.config(menu=menubar)


# window.mainloop()


import tkinter
from tkinter import *
from tkinter import ttk
import customtkinter
# import tkintermapview


# def entry() :
#     word = ent.get()
#     lbl['text'] = str(word)

def get_word() :
    global word
    global Tcar
    global TEssai
    global Tcar1
    Tcar = []
    word = entry_word.get()
    Tcar.append(word) 
    frmLeft.place_forget()
    frmCenter.place(x=420,y=40)

    TEssai = []
    for r in range(len(Tcar[0])) :
        TEssai.append('*')

    Tcar1 = []
    for j in range(len(Tcar[0])) :
        Tcar1.append(Tcar[0][j])

    entry_word.delete(0,END)

    lblCenter.place(x=100,y=0)
    entry_car.place(x=50,y=50)
    btn_car.place(x=110,y=100)

    lbl_Right.place(x=150,y=40)

    lbl_result['text'] = 'Statut'


# def get_caractere() :
#     car = entry_car.get()
#     return car




def all() :

    # word,Tcar,TEssai,Tcar1 = get_word()

    cond = False
    # car = str(input(Fore.WHITE + "Entrer un caractére : "))
    car = entry_car.get()
    entry_car.delete(0,END)
    for i in range(len(Tcar[0])) :
        if Tcar[0][i] == car :
            TEssai[i] = car
            cond = True 
            lbl_result['text'] = str(TEssai)
    if cond == False and int(lbl_Right['text']) > 0 :
            lbl_Right['text'] = str(int(lbl_Right['text']) - 1)
            if int(lbl_Right['text']) == 0 :
                pendu = PhotoImage(file='pendu 11.png')
                lblimg = Label(frm_all,image=pendu)
                PhotoImage(file="pendu 11.png")
                lblimg.pack()
            # elif int(lbl_Right['text']) == 2 :
            # elif int(lbl_Right['text']) == 3 :
            # elif int(lbl_Right['text']) == 4 :
            # elif int(lbl_Right['text']) == 5 :
            # elif int(lbl_Right['text']) == 6 :
            # elif int(lbl_Right['text']) == 7 :
            # elif int(lbl_Right['text']) == 8 :
            # elif int(lbl_Right['text']) == 9 :
            # elif int(lbl_Right['text']) == 10 :
            # elif int(lbl_Right['text']) == 11 :


    if Tcar1 == TEssai :
        lbl_result['text'] = '$$$$ You Win $$$$'
        lblCenter.place_forget()
        entry_car.place_forget()
        btn_car.place_forget()
        fin = True


    elif int(lbl_Right['text']) == 0 and Tcar != TEssai :
        lbl_result['text'] = 'You lost ' + ' "' + str(word) + '" '
        lblCenter.place_forget()
        entry_car.place_forget()
        btn_car.place_forget()
        fin = True







window = Tk()
window.title('Jeu de Pendu')
window.geometry('1200x750')
window.resizable(False, False)
window['bg'] = "#333"



# Enter a word to left
frmLeft = Frame(width=360,height=150,bg='#444')
frmLeft.place(x=20,y=40)

lblLeft = Label(frmLeft,text='Enter a word',font=('Arial',15),bg='#444',fg='#fff')
lblLeft.place(x=120,y=0)

entry_word = Entry(frmLeft,font=('Arial',17),justify='center')
entry_word.place(x=50,y=50)

btn_word = customtkinter.CTkButton(master=frmLeft,text='Submit',corner_radius=40,font=('Arial',20),command=get_word)
btn_word.place(x=110,y=100)




# Enter a caractére to center
frmCenter = Frame(width=360,height=150,bg='#444')


lblCenter = Label(frmCenter,text='Enter a caractére',font=('Arial',15),bg='#444',fg='#fff')


entry_car = Entry(frmCenter,font=('Arial',17),justify='center')


btn_car = customtkinter.CTkButton(master=frmCenter,text='Submit',corner_radius=40,font=('Arial',20),command=all)





# Essai to right
frmRight = Frame(width=360,height=150,bg='#444')
frmRight.place(x=820,y=40)

lbl_Right = Label(frmRight,text='11',font=('Arial',45),bg='#444',fg='#fff')




frm_all = Frame(height=500,width=850,bg='#fff')
frm_all.place(x=180,y=210)

frm_result = Frame(frm_all,height=80,width=840,bg='#ae775f')
frm_result.place(x=5,y=5)

lbl_result = Label(frm_result,text='Statut',height=2,width=45,font=('Arial',25),bg='#444',fg='#fff')
lbl_result.place(x=0,y=0)

frm_pendu = Frame(frm_all,height=410,width=850,bg='#af4')
frm_pendu.place(x=0,y=90)

window.mainloop()

