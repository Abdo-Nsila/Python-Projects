from figure import *

class Cercle(Figure) :

    def __init__(self, centre=None, couleur=None , rayon=None):
        super().__init__(centre, couleur)
        self.__rayon = rayon

    def saisir(self):
        print("\n_______________Crecle_____________")
        super().saisir()
        self.__rayon = float(input("Rayon : "))

    def perimetre(self):
        p = (self.__rayon**2) * 3.14
        return p
    
    def affichage(self):
        string = super().affichage()
        return string + f"Le Perimetre: {self.perimetre()}"
    
    @property
    def rayon(self) :
        return self.__rayon
    @rayon.setter
    def rayon(self , valeur) :
        self.__rayon = valeur
