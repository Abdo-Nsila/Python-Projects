import random
import time

def random_number() :
    return random.randint(1, 6,)
# while True :
#     time.sleep(0.5)




def Player_vs_Player(gamer1,gamer2) :
    score1 = 0
    score2 = 0
    while True :
        print("\n")
        print("                   |\__/\__/\__/\__/| ",gamer1," |\__/\__/\__/\__/| \n")
        input("                                 Tape to start                  ")
        num1 = random_number()
        print("______________________________________/","\\_________________________________")
        print("                                      ",num1)
        print("__________________________________________________________________________")


        print("\n")
        print("                   |\__/\__/\__/\__/| ",gamer2," |\__/\__/\__/\__/| \n")
        input("                                 Tape to start                  ")
        num2 = random_number()
        print("______________________________________/","\\_________________________________")
        print("                                      ",num2)
        print("__________________________________________________________________________")
        print("\n"*4)

        if num1 > num2 :
            score1 += 1
            print(num1)
            print("__________________________________$$$$     ",gamer1," win      $$$$__________________________________\n")
            print("       |\__/\__/Score of ",gamer1," : ",score1,"                             ","|\__/\__/Score of ",gamer2," : ",score2) 
        elif num2 > num1 :
            score2 += 1
            print(num2)
            print("__________________________________$$$$     ",gamer2," win      $$$$___________________________________\n")
            print("       |\__/\__/Score of ",gamer1," : ",score1,"                             ","|\__/\__/Score of ",gamer2," : ",score2) 
        else :
            print("______________________________________________¤ Equal ¤____________________________________\n")
            print("       |\__/\__/Score of Gamer 1 : ",score1,"                             ","|\__/\__/Score of Gamer 2 : ",score2) 

        if score1 == 10 :
            print("\n"*2)
            print("===================================================================================")
            print("                           $$$$     ",gamer1," WIN      $$$$                       ")
            print("===================================================================================")
            print("\n"*2)
            break
        elif score2 == 10 :
            print("\n"*2)
            print("===================================================================================")
            print("                           $$$$     ",gamer2," WIN      $$$$                       ")
            print("===================================================================================")
            print("\n"*2)
            break




def Player_vs_com(gamer1) :
    score1 = 0
    score2 = 0
    while True :
        print("\n")
        print("                   |\__/\__/\__/\__/| ",gamer1," |\__/\__/\__/\__/| \n")
        input("                                 Tape to start                  ")
        num1 = random_number()
        print("______________________________________/","\\_________________________________")
        print("                                      ",num1)
        print("__________________________________________________________________________")


        print("\n")
        time.sleep(0.8)
        print("                   |\__/\__/\__/\__/| ",gamer2," |\__/\__/\__/\__/| \n")
        # input("                                 Tape to start                  ")
        num2 = random_number()
        print("______________________________________/","\\_________________________________")
        print("                                      ",num2)
        print("__________________________________________________________________________")
        print("\n"*4)

        if num1 > num2 :
            score1 += 1
            print(num1)
            print("__________________________________$$$$     ",gamer1," win      $$$$__________________________________\n")
            print("       |\__/\__/Score of ",gamer1," : ",score1,"                             ","|\__/\__/Score of ",gamer2," : ",score2) 
        elif num2 > num1 :
            score2 += 1
            print(num2)
            print("__________________________________$$$$     ",gamer2," win      $$$$___________________________________\n")
            print("       |\__/\__/Score of ",gamer1," : ",score1,"                             ","|\__/\__/Score of ",gamer2," : ",score2) 
        else :
            print("______________________________________________¤ Equal ¤____________________________________\n")
            print("       |\__/\__/Score of Gamer 1 : ",score1,"                             ","|\__/\__/Score of Gamer 2 : ",score2) 

        if score1 == 10 :
            print("\n"*2)
            print("===================================================================================")
            print("                           $$$$     ",gamer1," WIN      $$$$                       ")
            print("===================================================================================")
            print("\n"*2)
            break
        elif score2 == 10 :
            print("\n"*2)
            print("===================================================================================")
            print("                           $$$$     ",gamer2," WIN      $$$$                       ")
            print("===================================================================================")
            print("\n"*2)
            break




def com_vs_com() :
    gamer1 = "com 1"
    gamer2 = "com 2"
    score1 = 0
    score2 = 0
    while True :
        print("\n")
        time.sleep(2)
        print("                   |\__/\__/\__/\__/| ",gamer1," |\__/\__/\__/\__/| \n")
        # input("                                 Tape to start                  ")
        num1 = random_number()
        print("______________________________________/","\\_________________________________")
        print("                                      ",num1)
        print("__________________________________________________________________________")


        print("\n")
        time.sleep(0.8)
        print("                   |\__/\__/\__/\__/| ",gamer2," |\__/\__/\__/\__/| \n")
        # input("                                 Tape to start                  ")
        num2 = random_number()
        print("______________________________________/","\\_________________________________")
        print("                                      ",num2)
        print("__________________________________________________________________________")
        print("\n"*4)

        if num1 > num2 :
            score1 += 1
            print(num1)
            print("__________________________________$$$$     ",gamer1," win      $$$$__________________________________\n")
            print("       |\__/\__/Score of ",gamer1," : ",score1,"                             ","|\__/\__/Score of ",gamer2," : ",score2) 
        elif num2 > num1 :
            score2 += 1
            print(num2)
            print("__________________________________$$$$     ",gamer2," win      $$$$___________________________________\n")
            print("       |\__/\__/Score of ",gamer1," : ",score1,"                             ","|\__/\__/Score of ",gamer2," : ",score2) 
        else :
            print("______________________________________________¤ Equal ¤____________________________________\n")
            print("       |\__/\__/Score of Gamer 1 : ",score1,"                             ","|\__/\__/Score of Gamer 2 : ",score2) 

        if score1 == 10 :
            print("\n"*2)
            print("===================================================================================")
            print("                           $$$$     ",gamer1," WIN      $$$$                       ")
            print("===================================================================================")
            print("\n"*2)
            break
        elif score2 == 10 :
            print("\n"*2)
            print("===================================================================================")
            print("                           $$$$     ",gamer2," WIN      $$$$                       ")
            print("===================================================================================")
            print("\n"*2)
            break



while True :
    print("\n"*3)
    choix = int(input("                    Player 1   vs    Player 2    [Enter : 1] \n \
                        Player   vs    com         [Enter : 2]\n \
                        com  vs    com         [Enter : 3] \n \
                        Back                  [Enter 0] \n \
                                    Your chose : "))


    if choix == 1 :
        print("\n"*2)
        gamer1 = str(input("Name of player 1 : "))
        gamer2 = str(input("Name of player 2 : "))
        Player_vs_Player(gamer1,gamer2)
    elif choix == 2 :
        gamer1 = str(input("Name of player 1 : "))
        print("\n"*2)
        Player_vs_com(gamer1)
    elif choix == 3 :
        com_vs_com()
    elif choix == 0 :
        break
    else :
        print("              Command is not found     ):")
        continue