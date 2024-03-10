from service import *

class Entreprise :

    def __init__(self,nom=None) :
        self.__nom = nom
        self.__l_service = []
        n = int(input("Entrer le nombre de services : "))
        for i in range(n) :
            self.__l_service.append(Service.ajouter())

    def afficher(self) :
        string = ""
        for i in self.__l_service :
            string += i.afficher()
        return f"L'Entreprise {self.__nom} a des services : \n" + string

