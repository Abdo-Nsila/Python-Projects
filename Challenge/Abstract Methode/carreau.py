from figure import *


class Carreau(Figure):
    def __init__(self, cote: float = None):
        self.__cote = cote

    def saisir(self):
        print("\n_______________Carreau_____________")
        self.__cote = float(input("Cote : "))

    def perimetre(self):
        p = self.__cote * 4
        return p

    def affichage(self):
        return f"Le Perimetre du Carreau: {self.perimetre()}"

    @property
    def cote(self):
        return self.__cote

    @cote.setter
    def cote(self, valeur):
        self.__cote = valeur
