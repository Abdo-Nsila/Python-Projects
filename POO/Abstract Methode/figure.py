from abc import ABC , abstractclassmethod
from colorama import Fore

class Figure(ABC) :

    def __init__(self , centre=None , couleur=None ) :
        super().__init__()
        self.__centre = centre
        self.__couleur = couleur

    def saisir(self) :
        self.__centre = str(input("Center du figure (x,y) : "))
        self.__couleur = (input("Couleur (GREEN,BLUE,YELLOW,MAGENTA) : "))


    @abstractclassmethod
    def perimetre(self) :
        pass

    def affichage(self) :

        if self.couleur == "GREEN" :
            return (f"Le centre: {self.centre}   La couleur: {Fore.LIGHTGREEN_EX}{self.couleur}{Fore.RESET}")
        elif self.couleur == "BLUE" :
            return (f"Le centre: {self.centre}   La couleur: {Fore.LIGHTBLUE_EX}{self.couleur}{Fore.RESET}")
        elif self.couleur == "YELLOW" :
            return (f"Le centre: {self.centre}   La couleur: {Fore.LIGHTYELLOW_EX}{self.couleur}{Fore.RESET}")
        elif self.couleur == "BLUE" :
            return (f"Le centre: {self.centre}   La couleur: {Fore.LIGHTBLUE_EX}{self.couleur}{Fore.RESET}")
        elif self.couleur == "MAGENTA" :
            return (f"Le centre: {self.centre}   La couleur: {Fore.LIGHTMAGENTA_EX}{self.couleur}{Fore.RESET}")
        else :
            return (f"Le centre: {self.centre}   La couleur: {Fore.LIGHTRED_EX}{self.couleur}{Fore.RESET}")

        


    
    @property
    def centre(self) :
        return self.__centre
    @centre.setter
    def centre(self , valeur) :
        self.__centre = valeur

    @property
    def couleur(self) :
        return self.__couleur
    @couleur.setter
    def couleur(self , valeur) :
        self.__couleur = valeur

    
