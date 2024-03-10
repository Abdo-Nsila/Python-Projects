import customtkinter as ctk
ctk.set_appearance_mode('systeme') #can set light or dark
ctk.set_default_color_theme("green") #themes: blue, dark-blue or green

class App(ctk.CTk) :

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #* initial window dimension :
        WIDTH = 1000
        HEIGHT = 600

        #* This code makes the window appear in the middle :
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width-WIDTH) / 2)
        y = int((screen_height-HEIGHT) / 2)

        self.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")
        self.resizable(False,False)
        self.title("Welcome")


app = App()
app.mainloop()       




