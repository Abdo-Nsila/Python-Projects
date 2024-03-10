from comparable import *

class Personne(Comparable) :

    def __init__(self,nom=None,age=None) :
        super().__init__()
        self.__nom = nom
        self.__age = age

    def saisir(self) :
        self.nom = input("Nom : ")
        self.age = input("Age : ")


    @classmethod
    def compareTo(self,obj1,obj2):
        super().compareTo(obj1,obj2)
        if obj1.age > obj2.age :
            return f"{obj1.nom} plus grand que {obj2.nom}"
        elif obj1.age < obj2.age :
            return f"{obj1.nom} moins grand que {obj2.nom}"
        elif obj1.age == obj2.age :
            return f"{obj1.nom} egale a {obj2.nom}"
        

    @property
    def nom(self) :
        return self.__nom
    @nom.setter
    def nom(self,valeur) :
        self.__nom = valeur

    @property
    def age(self) :
        return self.__age
    @age.setter
    def age(self,valeur) :
        self.__age = valeur
    


