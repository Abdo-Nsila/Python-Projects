from figure import *

class Triangle(Figure) :

    def __init__(self, cote1=None , cote2=None , cote3=None):
        self.__cote1 = cote1
        self.__cote2 = cote2
        self.__cote3 = cote3

    def saisir(self):
        print("\n_______________Triangle_____________")
        self.__cote1 = float(input("Cote1 : "))
        self.__cote2 = float(input("Cote2 : "))
        self.__cote3 = float(input("cote3 : "))

    def perimetre(self):
        p = (self.__cote1 + self.__cote2) * 2
        return p
    
    def affichage(self):
        return f"Le Perimetre du Triangle: {self.perimetre()}"
    
    @property
    def cote1(self) :
        return self.__cote1
    @cote1.setter
    def cote1(self , valeur) :
        self.__cote1 = valeur

    @property
    def cote2(self) :
        return self.__cote2
    @cote2.setter
    def cote2(self , valeur) :
        self.__cote2 = valeur

    @property
    def cote3(self) :
        return self.__cote3
    @cote3.setter
    def cote3(self , valeur) :
        self.__cote3 = valeur