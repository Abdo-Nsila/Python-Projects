from figure import *

class Cercle(Figure) :

    def __init__(self, rayon=None):
        self.__rayon = rayon

    def saisir(self):
        print("\n_______________Crecle_____________")
        self.__rayon = float(input("Rayon : "))

    def perimetre(self):
        p = (self.__rayon**2) * 3.14
        return p
    
    def affichage(self):
        return f"Le Perimetre du Crecle: {self.perimetre()}"
    
    @property
    def rayon(self) :
        return self.__rayon
    @rayon.setter
    def rayon(self , valeur) :
        self.__rayon = valeur
