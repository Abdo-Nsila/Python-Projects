from figure import *

class Carreau(Figure) :

    def __init__(self, centre=None, couleur=None , cote=None):
        super().__init__(centre, couleur)
        self.__cote = cote

    def saisir(self):
        print("\n_______________Carreau_____________")
        super().saisir()
        self.__cote = float(input("Cote : "))

    def perimetre(self):
        p = (self.__cote * 4) 
        return p
    
    def affichage(self):
        string = super().affichage()
        return string + f"Le Perimetre: {self.perimetre()}"
    
    @property
    def cote(self) :
        return self.__cote
    @cote.setter
    def cote(self , valeur) :
        self.__cote = valeur