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
    
    def dict_to_json(self) :
        data = {}
        data["Nom Service"] = self.__nomService
        data["Chef"] = [self.__Chef.dict_to_json()]
        return data

    @property
    def nomService(self) :
        return self.__nomService
    @nomService.setter
    def nomService(self,valeur) :
        self.nomService = valeur
    