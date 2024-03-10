import json
from colorama import Fore
import os
import tkinter
import customtkinter
from PIL import ImageTk, Image
import winsound
import time
import pyttsx3
text_speech = pyttsx3.init()

def play_sound(phrase) :
        text = phrase
        text_speech.say(text)
        text_speech.runAndWait()

# Start
os.system('cls')
text = "Bienvenue sur notre chatbot d'orientation !Pour commencer, veuillez répondre aux questions suivantes pour nous aider à mieux comprendre vos intérêts, vos compétences et vos motivations. Nous utiliserons ces informations pour vous suggérer des options de carrière qui correspondent à votre personnalité. \n\tNous vous remercions d'avance pour votre participation !"
print(f"\t{Fore.BLUE}Bienvenue sur notre chatbot d'orientation !Pour commencer, veuillez répondre aux questions suivantes pour nous aider à mieux comprendre vos intérêts, \n\tvos compétences et vos motivations. Nous utiliserons ces informations pour vous suggérer des options de carrière qui correspondent à votre personnalité. \n\tNous vous remercions d'avance pour votre participation !\n{Fore.RESET}")
# set sound
# play_sound(text)

name = input(f"{Fore.GREEN}Enter your name : {Fore.RESET}")

def play_sound(phrase) :
        text = phrase
        text_speech.say(text)
        text_speech.runAndWait()


os.system('cls')
# x = 6
# for i in range(5) :
#     x -= 1
#     print(f"\tHave fun ... [ {Fore.YELLOW}{x}{Fore.RESET} ]",end="\r")
#     time.sleep(1)

#open file and put it in info att after convert json format to dic
with open('Data_Q.json',"r") as f:
    info = json.load(f)


# bring Q and his As and notes of ansowers from json file
q_num = -1
def get_info():
    global q_num
    q_num += 1
    return [list(info)[q_num],info[list(info)[q_num]]] # E:[quesiton , [true,{"ch1":[0,1,0,1]}]

# show quesiont in screen and return answer
def display(q):
    os.system('cls')
    print(f"{Fore.YELLOW}{q[0]}")
    # set Question sound
    # play_sound(q[0])
    for i in range(len(list(q[1][1]))):
        print(f"{Fore.CYAN}\t{i+1}-",list(q[1][1])[i])
        # set choix sound
        # play_sound(list(q[1][1])[i])
    
    if q[1][0]:
        c = input(f"{Fore.LIGHTGREEN_EX}your choose(s) Multi choix enter for example 1,3,4,7 : {Fore.LIGHTWHITE_EX}")
        c = c.split(",")
        ans_select = {}
        for i in range(len(c)):
            ans_select[list(q[1][1])[int(c[i])-1]] =  q[1][1][list(q[1][1])[int(c[i])-1]]
        return [q[0],ans_select]

    c = int(input(f"{Fore.LIGHTGREEN_EX}your choose : {Fore.LIGHTWHITE_EX}"))
    ans_select = list(q[1][1])[c-1]
    # print([q[0],{ans_select:q[1][1][ans_select] }])
    return [q[0],{ans_select:q[1][1][ans_select] }] 
    

# best choi tab
final_tab = [0 for i in range(4)]
def filiers_notes(tab):
    global final_tab
    for i in range(len(final_tab)):
        final_tab[i] += tab[i]
    

# stock answers in csv file
def stock(data): # [q, {q1:[1,2,3,4]}]
    file = open("data.csv","a",encoding='utf-8')
    if q_num == 0:
        file.write(f"\nUsername: {name}\n")
    t = [0 for t in range(4) ]
    for i in range(len(list(data[1]))):
        for j in range(4):
            t[j] += data[1][list(data[1])[i]][j]
    filiers_notes(t)
    file.write(f"{data[0]};{list(data[1])};{t}\n")
    print(f"{Fore.RESET}")
    file.close()


# best filier
def best_filier():
    return final_tab.index(max(final_tab))

# conrole info 
def controller():
    q_Info = get_info()
    q_Ans = display(q_Info)
    
    stock(q_Ans)
    if q_num+1 < len(list(info)):
        controller()
        return

controller()
tab = ["Devellopement gigital","Infrascracture digital","Marketing Digital","Design"]
text = f"Merci d'avoir utilisé notre chatbot d'orientation ! En fonction de vos réponses, nous avons identifié l’option de carrière suivante qui correspond à vos intérêts, vos compétences et vos motivations : {tab[best_filier()]}. Nous vous encourageons à explorer cette option pour en savoir plus sur elle, et à consulter des professionnels pour obtenir des conseils sur la façon de poursuivre cette carrière. Nous espérons que cette expérience vous a été utile et vous a aidé à explorer de nouvelles idées pour votre avenir professionnel."
print(f"{os.system('cls')}{Fore.LIGHTBLUE_EX}Merci d'avoir utilisé notre chatbot d'orientation ! En fonction de vos réponses, nous avons identifié l’option de carrière suivante qui correspond à vos intérêts, vos compétences et vos motivations : {Fore.LIGHTGREEN_EX}{tab[best_filier()]}{Fore.LIGHTBLUE_EX}. Nous vous encourageons à explorer cette option pour en savoir plus sur elle, et à consulter des professionnels pour obtenir des conseils sur la façon de poursuivre cette carrière. Nous espérons que cette expérience vous a été utile et vous a aidé à explorer de nouvelles idées pour votre avenir professionnel.")
# play_sound(text)





customtkinter.set_appearance_mode('systeme') #can set light or dark
customtkinter.set_default_color_theme("green") #themes: blue, dark-blue or green

app = customtkinter.CTk() # creating custom tkinter window
app.geometry("800x500")
app.title("Login")


