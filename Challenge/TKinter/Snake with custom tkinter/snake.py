import customtkinter as ctk
import time
import random

ctk.set_appearance_mode("systeme")  # can set light or dark
ctk.set_default_color_theme("dark-blue")  # themes: blue, dark-blue or green


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.frms = []
        self.cords = []
        self.role = 2
        self.t = [
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
        self.WIDTH = 1000
        self.HEIGHT = 600

        # * This code makes the window appear in the middle :
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = int((screen_width - self.WIDTH) / 2)
        y = int((screen_height - self.HEIGHT) / 2)

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}+{x}+{y}")
        self.resizable(False, False)
        self.title("Welcome")

        self.frm = ctk.CTkFrame(self, height=20, width=20, fg_color="#fff")
        self.frm.place(x=0, y=0)
        self.frms.append(self.frm)
        self.cords.append([0, 0])

        self.bind("<Right>", self.right)
        self.bind("<Left>", self.left)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)

    def move(self, a, b, pos):
        while True:
            self.update()
            time.sleep(0.03)

            for i in range(len(self.cords) - 1, -1, -1):
                if i == 0:
                    self.cords[i][0] += a
                    x = self.cords[i][0]
                    self.cords[i][1] += b
                    y = self.cords[i][1]
                    self.frms[i].place(x=x, y=y)
                else:
                    self.cords[i][0] = self.cords[i - 1][0]
                    self.cords[i][1] = self.cords[i - 1][1]
                    x = self.cords[i][0]
                    y = self.cords[i][1]
                    self.frms[i].place(x=x, y=y)
            if pos == "r":
                if self.cords[0][0] > self.WIDTH:
                    self.cords[0][0] = 0
            elif pos == "l":
                if self.cords[0][0] < 0:
                    self.cords[0][0] = self.WIDTH
            elif pos == "u":
                if self.cords[0][1] < 0:
                    self.cords[0][1] = self.HEIGHT
            elif pos == "d":
                if self.cords[0][1] > self.HEIGHT:
                    self.cords[0][1] = 0

    def add_more(self):
        # t = ['#f00','#0f0','#00f','#ff0','#f0f','#0ff','#8f1','#888','#fff','#1f5ff3','#70d','#0d0','#adb','#248','#0f9','#a51','#548']
        color = random.choice(self.t)
        self.add_frm = ctk.CTkFrame(self, height=20, width=20, fg_color=color)
        self.frms.append(self.add_frm)
        self.cords.append([0, 0])

    def add(self, x=0):
        [self.add_more() for i in range(x)]

    def right(self, event):
        if self.role != 0:
            self.role = 0
            self.move(20, 0, "r")

    def left(self, event):
        if self.role != 0:
            self.role = 0
            self.move(-20, 0, "l")

    def up(self, event):
        if self.role != 1:
            self.role = 1
            self.move(0, -20, "u")

    def down(self, event):
        if self.role != 1:
            self.role = 1
            self.move(0, 20, "d")


app = App()
app.add(50)
app.mainloop()
