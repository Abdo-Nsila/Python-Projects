from personne import *
from colorama import Fore, Back, Style



while True :

    choix = int(input(f"                                            {Fore.YELLOW}[Menu Des Choix]\n\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Ajouter Personne {Fore.BLUE}(enter 1)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Afficher Les Personnes {Fore.BLUE}(enter 2)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Modifier  {Fore.BLUE}(enter 3)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Supprimer {Fore.BLUE}(enter 4)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Chercher {Fore.BLUE}(enter 5)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Compter  {Fore.BLUE}(enter 6)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Categorie {Fore.BLUE}(enter 7)\n\
                                -----------------------------------------\n{Fore.MAGENTA}"))

    if choix == 1 :
        num = int(input(f"{Fore.LIGHTGREEN_EX} ______________________________________________/Entrer nombre de Personne a ajouter :\\____________________________________________ {Fore.WHITE}\n"))
        for i in range(num) :
            print(f"                                {Fore.YELLOW}|-----------------------------------|")
            print(f"                                  {Fore.YELLOW}|----------Personne {i+1}----------|{Fore.WHITE}\n")
            Personne.ajouter()

    elif choix == 2 :
        Personne.affichage()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")

    elif choix == 3 :
        Personne.modifier(input("code : "),input("nom : "))
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")

    elif choix == 4 :
        Personne.supprimer()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 5 :
        Personne.chercher()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 6 :
        Personne.compter()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 7 :
        Personne.categorie()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")
