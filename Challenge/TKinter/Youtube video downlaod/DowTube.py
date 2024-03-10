import customtkinter
import tkinter
from pytube import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

# ----------------------- Install Library ----------------------
#? pip install pytube
#? pip install pillow








#! --------------------------------------------------First Window--------------------------------------------------------------------
def create_window() :
    global window

    customtkinter.set_appearance_mode('systeme') #can set light or dark
    customtkinter.set_default_color_theme("blue") #themes: blue, dark-blue or green

    window = customtkinter.CTk()
    window.title("PyTube")
    window.iconbitmap('D:\Files\SCHOOL\Python\Challenge\TKinter\Youtube video downlaod\downlod.ico')

    #* Center a window
    screen_height = window.winfo_screenheight()
    screen_width = window.winfo_screenwidth()
    window_width = 1280
    window_height = 720
    padx = int((screen_width-window_width) / 2)
    pady = int((screen_height-window_height) / 2)
    window.geometry(f"{window_width}x{window_height}+{padx}+{pady}")

def first_window() :

    create_window()

    img1 = ImageTk.PhotoImage(Image.open('D:\Files\SCHOOL\Python\Challenge\TKinter\Youtube video downlaod\youtube_logo.png').resize((250,250)), Image.ANTIALIAS)
    lbl_logo = customtkinter.CTkLabel(window,text="",image=img1)
    lbl_logo.pack(pady=20,fill='both',expand=False)

    frm1 = customtkinter.CTkFrame(master=window,corner_radius=10,height=500)
    frm1.pack(padx=60,pady=10,anchor=tkinter.CENTER,fill='both',expand=True)

    lbl = customtkinter.CTkLabel(frm1,text="Past Video URL :",font=("Arial",60))
    lbl.pack(pady=20,anchor=tkinter.CENTER)

    entry = customtkinter.CTkEntry(frm1,font=("Arial",20),height=40,width=800)
    entry.pack(pady=20,anchor=tkinter.CENTER)


    btn_url = customtkinter.CTkButton(frm1,text="Submit",font=("Arial",40),height=100,width=300,command= lambda : second_window(entry.get()))
    btn_url.pack(pady=60,anchor=tkinter.CENTER)


    frm2 = customtkinter.CTkFrame(master=frm1,corner_radius=10,height=50)
    frm2.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)
    lbl = customtkinter.CTkLabel(frm2,text="Light       Dark                       ")
    lbl.pack(anchor=tkinter.CENTER)
    mode_switch = customtkinter.CTkSwitch(frm2, text="",
                                        command=lambda: customtkinter.set_appearance_mode("dark" if mode_switch.get() == 0 else "light"))
    mode_switch.pack(anchor=tkinter.CENTER)

    window.mainloop()














#! --------------------------------------------------Second Window--------------------------------------------------------------------
def create_app() :
    global app

    customtkinter.set_appearance_mode('systeme') #can set light or dark
    customtkinter.set_default_color_theme("blue") #themes: blue, dark-blue or green

    app = customtkinter.CTk()
    app.title("PyTube")
    app.iconbitmap('D:\Files\SCHOOL\Python\Challenge\TKinter\Youtube video downlaod\downlod.ico')

    #* Center a app
    screen_height = app.winfo_screenheight()
    screen_width = app.winfo_screenwidth()
    app_width = 1280
    app_height = 720
    padx = int((screen_width-app_width) / 2)
    pady = int((screen_height-app_height) / 2)
    app.geometry(f"{app_width}x{app_height}+{padx}+{pady}")
    app.resizable(False,False)


def second_window(url) :
    #! https://youtu.be/iUIqPXn4zKs  get image
    global yt
    window.destroy()
    print(url)
    yt = YouTube(url)
    create_app()

    frm = customtkinter.CTkFrame(app,height=600,width=1200)
    frm.pack(padx=20,pady=20,anchor=tkinter.CENTER,fill='both',expand=True)


    #! ------------------------------------------------------------------------------------------------------
    frm1 = customtkinter.CTkFrame(frm,height=600,width=330)
    frm1.grid(row=0,column=0, padx=20, pady=20, sticky="ew")

    lbl_id = customtkinter.CTkLabel(frm1,text=f"Id_video:\n",font=('Arial',30),text_color="#c02")
    lbl_age = customtkinter.CTkLabel(frm1,text=f"Restricted:\n",font=('Arial',30),text_color="#c02")
    lbl_channel = customtkinter.CTkLabel(frm1,text=f"Channel:\n",font=('Arial',30),text_color="#c02")
    lbl_PubDate = customtkinter.CTkLabel(frm1,text=f"Published Date:\n",font=('Arial',30),text_color="#c02")
    lbl_views = customtkinter.CTkLabel(frm1,text=f"Number of views:\n",font=('Arial',30),text_color="#c02")
    lbl_duree = customtkinter.CTkLabel(frm1,text=f"Length of video:\n",font=('Arial',30),text_color="#c02")
    
    lbl_id_main = customtkinter.CTkLabel(frm1,text=f"{yt.video_id}\n",font=('Segoe UI',22))
    lbl_age_main = customtkinter.CTkLabel(frm1,text=f"{yt.age_restricted}\n",font=('Segoe UI',22))
    lbl_channel_main = customtkinter.CTkLabel(frm1,text=f"{yt.author}\n",font=('Segoe UI',22))
    lbl_PubDate_main = customtkinter.CTkLabel(frm1,text=f"{yt.publish_date.strftime('%Y-%m-%d')}\n",font=('Segoe UI',22))
    lbl_views_main = customtkinter.CTkLabel(frm1,text=f"{yt.views}\n",font=('Segoe UI',22))
    lbl_duree_main = customtkinter.CTkLabel(frm1,text=f"{yt.length}\n",font=('Segoe UI',22))

    t_lbl_header = [lbl_id,lbl_age,lbl_channel,lbl_PubDate,lbl_views,lbl_duree]
    t_lbl_main = [lbl_id_main,lbl_age_main,lbl_channel_main,lbl_PubDate_main,lbl_views_main,lbl_duree_main]

    y = 0.1
    for i in range(len(t_lbl_header)) :
        t_lbl_header[i].place(relx=0.5,rely=y,anchor=tkinter.CENTER) 
        t_lbl_main[i].place(relx=0.5,rely=y+0.05,anchor=tkinter.CENTER) 
        y += 0.15


    #! ------------------------------------------------------------------------------------------------------
    def directory() :
        dir = filedialog.askdirectory()
        print(dir)
        var_path.set(dir)

    frm2 = customtkinter.CTkFrame(frm,height=600,width=480)
    frm2.grid(row=0,column=1, pady=20, sticky="ew")

    lbl_tiltle_header = customtkinter.CTkLabel(frm2,text=f"Title:",font=('Arial',30),text_color="#c02")
    lbl_tiltle_header.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
    lbl_tiltle_main = customtkinter.CTkLabel(frm2,text=f"{yt.title}",font=('Segoe UI',15))
    lbl_tiltle_main.place(relx=0.5,rely=0.15,anchor=tkinter.CENTER)

    frm_image = customtkinter.CTkFrame(master=frm2)
    frm_image.place(relx=0.5,rely=0.35,anchor=tkinter.CENTER)
    img2 = ImageTk.PhotoImage(Image.open('D:\Files\SCHOOL\Python\Challenge\TKinter\Youtube video downlaod\downlod.png').resize((150,150)), Image.ANTIALIAS)
    lbl_logo = customtkinter.CTkLabel(master=frm_image,text="",image=img2,bg_color="#333")
    lbl_logo.pack(fill='both',expand=False)

    lbl_direcroty = customtkinter.CTkLabel(frm2,text=f"Select the path where you want to save",font=('Segoe UI',25),text_color="#0af")
    lbl_direcroty.place(relx=0.5,rely=0.58,anchor=tkinter.CENTER)

    var_path = customtkinter.StringVar()
    entery_browse = customtkinter.CTkEntry(frm2,textvariable=var_path,font=('Segoe UI',12),placeholder_text="",width=300,text_color="#0af")
    entery_browse.place(relx=0.32,rely=0.7,anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(frm2, text="Browse", command=directory)  # <------
    button.place(relx=0.8,rely=0.7,anchor=tkinter.CENTER)

    mode_switch = customtkinter.CTkSwitch(frm2, text="",
                                        command=lambda: (customtkinter.set_appearance_mode("dark" if mode_switch.get() == 0 else "light") , lbl_logo.configure(bg_color=("#333" if mode_switch.get() == 0 else "#ccc"))))
    mode_switch.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)

    #! ------------------------------------------------------------------------------------------------------
    def list_resolution() :

        #* Get all resolution => .mp4
        global all
        x = yt.streams.filter(file_extension='mp4',progressive=True)
        all_res = [str(i).split(' ')[3][5:-1] for i in x]
        return all_res

    frm3 = customtkinter.CTkFrame(frm,height=600,width=350)
    frm3.grid(row=0,column=2, padx=20, pady=20, sticky="ew")

    lbl_direcroty = customtkinter.CTkLabel(frm3,text=f"Choose the quality you want to download",font=('Segoe UI',18),text_color="#0af")
    lbl_direcroty.place(relx=0.5,rely=0.3,anchor=tkinter.CENTER)

    combobox_var = customtkinter.StringVar(value="Select Resolution")  # set initial value
    combobox = customtkinter.CTkComboBox(master=frm3,
                                     values=list_resolution(),font=('Segoe UI',18),width=250,
                                     variable=combobox_var)
    combobox.place(relx=0.5,rely=0.4,anchor=tkinter.CENTER)

    def download():
        os.system('cls')

        save_path = var_path.get()
        res = combobox_var.get()
        
        print(save_path)
        print(res)


        #! Customize resolution => .mp4
        yt.streams.get_by_resolution(resolution=res).download(save_path)
        print("Video successfullly downloaded")
        app.destroy()
        first_window()


    img3 = ImageTk.PhotoImage(Image.open('D:\Files\SCHOOL\Python\Challenge\TKinter\Youtube video downlaod\downlod.png').resize((50,50)), Image.ANTIALIAS)
    btn_submit = customtkinter.CTkButton(frm3, text="Download", command=download,font=('Segoe UI',30),height=80,width=250,image=img3)
    btn_submit.place(relx=0.5,rely=0.8,anchor=tkinter.CENTER)

    os.system('cls')
    app.mainloop()

first_window()
