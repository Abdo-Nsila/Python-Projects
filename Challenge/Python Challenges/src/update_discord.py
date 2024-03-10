import time
import random
import customtkinter as ctk


ctk.set_appearance_mode("systeme")  # can set light or dark
ctk.set_default_color_theme("dark-blue")  # themes: blue, dark-blue or green


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.num = 3
        self.cond = False
        self.colors = [
            "#f00",
            "#0f0",
            "#00f",
            "#ff0",
            "#f0f",
            "#0ff",
            "#8f1",
            "#888",
            "#fff",
            "#1f5ff3",
            "#70d",
            "#0d0",
            "#adb",
            "#248",
            "#0f9",
            "#a51",
            "#548",
        ]
        # self.color = random.choice(self.t)

        # * initial window dimension :
        self.WIDTH = 400
        self.HEIGHT = 470

        # * This code makes the window appear in the middle :
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - self.WIDTH) / 2)
        y = int((screen_height - self.HEIGHT) / 2)

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")
        self.resizable(False, False)
        self.title("Welcome")

        # self.wm_attributes('-transparentcolor', '#333') 
        self.text = ctk.CTkLabel(self, text="",font=('Arial',15))
        self.text.place(relx=0.1, rely=0.4)
        
        # self.btn = ctk.CTkButton(self, text="Click me",command=self.retrying)
        # self.btn.place(relx=0.3, rely=0.5)
        self.retrying()

    def retrying(self):
        while True:
            self.text.place_forget()
            color = random.choice(self.colors)
            for i in range(self.num, -1, -1):
                self.update()
                time.sleep(1)
                t = f"Update Failed-retrying in {i} sec..."
                self.text = ctk.CTkLabel(self, text=t,font=('Arial',25),text_color=color)
                self.text.place(relx=0.15, rely=0.4)
            self.num += int(self.num / 2)
            if self.cond:
                print("Connection Success")
                break


app = App()
app.mainloop()

