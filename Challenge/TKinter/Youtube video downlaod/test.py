# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog

# interface = Tk()
# interface.geometry('500x350')

# def openfile():
#     a = filedialog.askdirectory()
#     # a = filedialog.askopenfilename()
#     lbl['text'] = a

# button = ttk.Button(interface, text="Open", command=openfile)  # <------
# button.grid(column=1, row=1)

# lbl = Label(text="")
# lbl.grid(column=2, row=1)

# interface.mainloop()


# # import required library
# import webbrowser
# from tkinter import *
# from tkinter import ttk

# # creating root
# root = Tk()

# # setting GUI title
# root.title("WebBrowsers")

# # setting GUI geometry
# root.geometry("660x660")

# # call webbrowser.open() function.
# button = ttk.Button(root, text="Open", command=lambda : webbrowser.open("www.instagram.com"))  # <------
# button.grid(column=1, row=1)
# root.mainloop()





# Import tkinter and webview libraries
from tkinter import *
import webview
  
# define an instance of tkinter
tk = Tk()
  
#  size of the window where we show our website
tk.geometry("1280x720")
  
# Open website
webview.create_window('Youtube', 'https://youtube.com')
webview.start()
tk.mainloop()




# import customtkinter

# app = customtkinter.CTk()
# app.geometry("660x660")

# combobox_var = customtkinter.StringVar(value="option 2")  # set initial value

# def combobox_callback(choice):
#     print("combobox dropdown clicked:", choice)

# combobox = customtkinter.CTkComboBox(master=app,
#                                      values=[f"option {i+1}" for i in range(200)],font=('Segoe UI',18),width=300,
#                                      command=combobox_callback,
#                                      variable=combobox_var)
# combobox.pack(padx=20, pady=10)

# app.mainloop()