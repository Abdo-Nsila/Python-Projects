import json
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
    
    def dict_to_json(self) :
        data = {}
        data["Nom Entreprise"] = self.__nom
        data["Service"] = []
        for i in self.__l_service :
            data["Service"].append(i.dict_to_json())
        print(data)

        ptr_json = open("D:/Files/SCHOOL/Python/POO/Entreprise/data of Entreprise/data.json" , 'w' , encoding='utf-8')
        json.dump(data , ptr_json)
        ptr_json.close()
