# Tcar = ['M','o','t']
# TEssai = ['*','*','*']
# Quand tu trouve un caractére TEssai = ['*','o','*']
# Si faux essai = essai + 1
# 5 --> essai
import colorama
from colorama import Fore, Back, Style
colorama.init()
import os
def all(Tcar) :

    TEssai = []
    print("\n"*40)

    for r in range(len(Tcar[0])) :
        TEssai.append('*')

    Tcar1 = []
    for j in range(len(Tcar[0])) :
        Tcar1.append(Tcar[0][j])


    essai = 0
    while True :
        cond = False
        car = str(input(Fore.WHITE + "Entrer un caractére : "))
        for i in range(len(Tcar[0])) :
            if Tcar[0][i] == car :
                TEssai[i] = car
                cond = True 
                print("")
                print(Fore.GREEN + "")
                print(TEssai)
                print("")
        if cond == False :
            essai += 1
            print("")
            essais = 11 - essai
            print("")
            print(Fore.RED + '     Essai rester : ',essais)
            if essai == 1 :
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("")
                print("                    ")
                print(Fore.RED + "__||________")
                print(Fore.RED + "------------")
            elif essai == 2 :
                print("")
                print("")
                print(Fore.RED + "  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 3 :
                print(Fore.RED + "|______________________")
                print("|----------------------")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 4 :
                print(Fore.RED + "|______________________")
                print("|----------------------")
                print("  || //")
                print("  ||//")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 5 :
                print(Fore.RED + "|______________________")
                print("|----------------------")
                print("  || //             |")
                print("  ||//")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 6 :
                print(Fore.RED + "|______________________")
                print("|----------------------")
                print("  || //            |")
                print("  ||//             Q")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 7 :
                print(Fore.RED + "|______________________")
                print("|----------------------")
                print("  || //             |")
                print("  ||//              Q")
                print("  ||                |")
                print("  ||                |")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 8 :
                print(Fore.RED + "|______________________")
                print("|----------------------")
                print("  || //             |  ")
                print("  ||//              Q  ")
                print("  ||               /|  ")
                print("  ||              / |  ")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 9 :
                print(Fore.RED + "|______________________   ")
                print("|----------------------  ")
                print("  || //             |    ")
                print("  ||//              Q    ")
                print("  ||               /|\\  ")
                print("  ||              / | \\ ")
                print("  ||")
                print("  ||")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 10 :
                print(Fore.RED + "|______________________")
                print("|----------------------")
                print("  || //             |")
                print("  ||//              Q")
                print("  ||               /|\\")
                print("  ||              / |")
                print("  ||               /")
                print("  ||              /")
                print("  ||")
                print("__||________")
                print("------------")
            elif essai == 11 :
                print(Fore.RED + "|______________________  ")
                print("|----------------------  ")
                print("  || //             |    ")
                print("  ||//              Q    ")
                print("  ||               /|\\  ")
                print("  ||              / | \\ ")
                print("  ||               / \\  ")
                print("  ||              /   \\ ")
                print("__||________")
                print("------------")
            print("")
        if Tcar1 == TEssai :
            print("")
            print(Fore.YELLOW + "||---------------------------------------------------------------||")
            print('||         $$$$$     You Win, You are a Monster     $$$$$        ||')
            print("||                                                               ||")
            print("||                                                               ||")
            print("||                       *                 *                     ||")
            print("||                     * * *             * * *                   ||")
            print("||                       *                 *                     ||")
            print("||                               ^                               ||")
            print("||                              / \\                              ||")
            print("||                                                               ||")
            print("||                                                               ||")
            print("||              ' '                              ' '             ||")
            print("||              '  '                            '  '             ||")
            print("||               ' ''                          '' '              ||")
            print("||                 '' '''''  \        /  ''''' ''                ||")
            print("||                    ''''    ''''''''   ''''                    ||")
            print("||                           \        /                          ||")
            print("||                            ''''''''                           ||")
            print("||                                                               ||")
            print("||---------------------------------------------------------------||")
            print("\n"*5)
            input(Fore.BLUE + "                           Train Again :")
            print("\n"*5)
            os.system('cls')
            break

        elif essai == 11 and Tcar != TEssai :
            print()
            print(Fore.RED + "||-----------------------------------------||")
            print('||        !!!!!     You lost    !!!!!      ||')
            print('||          Le mot est : <<<' + Fore.YELLOW + mot + Fore.RED + ">>>        ||")
            print("||-----------------------------------------||")
            print("\n"*5)
            input(Fore.BLUE + "                           Train Again :")
            print("\n"*5)
            os.system('cls')
            break



def MotValid(mot, n) :
    cond = False
    if (n >= 4) and (n <= 25) :
        cond = True
        for i in range(n) :
            if ord(mot[i]) < 65 or ord(mot[i]) > 90 :
                cond = False
                break
    if cond == False :
        return False
    elif cond == True :
        return True

while True :
    Tcar = []
    print('\n'*5)
    mot = str(input(Fore.BLUE + "|\__/\__/\__/\__/ Entrer un Mot \__/\__/\__/\__/| : "))
    os.system('cls')

    Tcar.append(mot)
    n = len(mot)

    if MotValid(mot,n) == False :
        print(Fore.RED + "!!!!   Le mot--|",mot,"|--est invalid   !!!!")
        print("\n","\n")
    elif MotValid(mot,n) == True :
        # print("le mot--|",str(mot),"|--est valid." )
        all(Tcar)
