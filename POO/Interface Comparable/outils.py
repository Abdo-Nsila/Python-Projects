from comparable import *

class Outils(Comparable) :

    def __init__(self,nom=None,langueur=None,prix=None) :
        super().__init__()
        self.__nom = nom
        self.__langueur = langueur
        self.__prix = prix

    def saisir(self) :
        self.nom = input("Nom : ")
        self.langueur = input("Langueur : ") 
        self.prix = input("Prix : ") 

    @classmethod
    def compareTo(self,obj1,obj2):
        super().compareTo(obj1,obj2)
        if obj1.langueur > obj2.langueur :
            return f"{obj1.nom} plus large que {obj2.nom}"
        elif obj1.langueur < obj2.langueur :
            return f"{obj1.nom} moins large que {obj2.nom}"
        else :
            return f"{obj1.nom} egale {obj2.nom}"
        
    @property
    def nom(self) :
        return self.__nom
    @nom.setter
    def nom(self,valeur) :
        self.__nom = valeur

    @property
    def langueur(self) :
        return self.__langueur
    @langueur.setter
    def langueur(self,valeur) :
        self.__langueur = valeur

    @property
    def prix(self) :
        return self.__prix
    @prix.setter
    def prix(self,valeur) :
        self.__prix = valeur
    