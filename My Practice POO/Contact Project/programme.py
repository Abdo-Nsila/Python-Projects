from colorama import Fore, Back, Style
import os
 
while True :
    choix = int(input(f"                                            {Fore.YELLOW}[Menu of Chose]\n\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Create Contacts {Fore.BLUE}(enter 1)\n\
                                ________________________________________\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Display Contacts {Fore.BLUE}(enter 2)\n\
                                ________________________________________\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Modify Contact {Fore.BLUE}(enter 3)\n\
                                ________________________________________\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Remove Contact {Fore.BLUE}(enter 4)\n\
                                ________________________________________\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Search Contact {Fore.BLUE}(enter 5)\n\
                                ________________________________________\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Number of Contact {Fore.BLUE}(enter 6)\n\
                                ________________________________________\n{Fore.LIGHTWHITE_EX}{Fore.LIGHTWHITE_EX}"))
    os.system('cls')
    if choix == 1 :
            from user import *
            # print(f"                                {Fore.YELLOW}|-----------------------------------|")
            # print(f"                                  {Fore.YELLOW}|----------Stagiaire {i+1}----------|{Fore.WHITE}\n")
            us = User()

    elif choix == 2 :
        print(us.display())
        print(f"\n{Fore.YELLOW}         |-----------------------------------------------------------------------------------------------------------------------------------------------|{Fore.WHITE}\n")

    elif choix == 3 :
        us.modify()
        print(f"\n{Fore.YELLOW}         |-----------------------------------------------------------------------------------------------------------------------------------------------|{Fore.WHITE}\n")

    elif choix == 4 :
        us.remove()
        print(f"\n{Fore.YELLOW}         |-----------------------------------------------------------------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 5 :
        us.search()
        print(f"\n{Fore.YELLOW}         |-----------------------------------------------------------------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 6 :
        us.count()
        print(f"\n{Fore.YELLOW}         |-----------------------------------------------------------------------------------------------------------------------------------------------|{Fore.WHITE}\n")

