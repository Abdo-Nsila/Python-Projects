from figure import *

class Rectangle(Figure) :

    def __init__(self, centre=None, couleur=None , largeur=None , longeur=None):
        super().__init__(centre, couleur)
        self.__largeur = largeur
        self.__longeur = longeur

    def saisir(self):
        print("\n_______________Rectangle_____________")
        super().saisir()
        self.__largeur = float(input("Largeur : "))
        self.__longeur = float(input("Longeur : "))

    def perimetre(self):
        p = (self.__largeur + self.__longeur) * 2
        return p
    
    def affichage(self):
        string = super().affichage()
        return string + f" Le Perimetre: {self.perimetre()}"
    
    @property
    def largeur(self) :
        return self.__largeur
    @largeur.setter
    def largeur(self , valeur) :
        self.__largeur = valeur

    @property
    def longeur(self) :
        return self.__longeur
    @longeur.setter
    def longeur(self , valeur) :
        self.__longeur = valeur

