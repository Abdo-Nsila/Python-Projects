from stagiaire import *
from colorama import Fore, Back, Style

# Tab = []
# for i in range(2) :
#     stg = Stagiaire()
#     stg.saisir()
#     Tab.append(stg)

# for j in range(2) :
#     print(Tab[j].afficher())

# [+]

while True :

    choix = int(input(f"                                            {Fore.YELLOW}[Menu Des Choix]\n\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Ajouter Stagiaire {Fore.BLUE}(enter 1)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Afficher Les Stagiaires {Fore.BLUE}(enter 2)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Afficher Super {Fore.BLUE}(enter 3)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Calculer la moyenne {Fore.BLUE}(enter 4)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Chercher un Stagiaire {Fore.BLUE}(enter 5)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Modifier la note {Fore.BLUE}(enter 6)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Supprimer un Stagiaire {Fore.BLUE}(enter 7)\n\
                                ----------------------------------------\n\
                                {Fore.CYAN}[{Fore.MAGENTA}+{Fore.CYAN}] {Fore.WHITE}Afficher le nombre du Stagiaire {Fore.BLUE}(enter 8)\n\
                                -----------------------------------------\n{Fore.MAGENTA}"))

    if choix == 1 :
        num = int(input(f"{Fore.LIGHTGREEN_EX} ______________________________________________/Entrer nombre de Stagiaire a ajouter :\\____________________________________________ {Fore.WHITE}\n"))
        for i in range(num) :
            print(f"                                {Fore.YELLOW}|-----------------------------------|")
            print(f"                                  {Fore.YELLOW}|----------Stagiaire {i+1}----------|{Fore.WHITE}\n")
            Stagiaire.ajouter()

    elif choix == 2 :
        Stagiaire.afficher()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")

    elif choix == 3 :
        Stagiaire.affiche_Super()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")

    elif choix == 4 :
        Stagiaire.calculer()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 5 :
        Stagiaire.chercher()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 6 :
        Stagiaire.modifier()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 7 :
        Stagiaire.supprimer()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")


    elif choix == 8 :
        Stagiaire.afficher_nbr_Stg()
        print(f"\n{Fore.YELLOW}|-------------------------------------------------------------------------------------|{Fore.WHITE}\n")
