from chef import *

class Service :
    

    def __init__(self,nomService=None) :
        self.__nomService = nomService
        self.__Chef = Chef.ajouter()

    def ajouter() :
        nomService = str(input("Nom du Service : "))
        serv = Service(nomService)
        return serv
    
    def afficher(self) :
        return f"Le nom de service est {self.__nomService} \n {self.__Chef.afficher()} \n"
    