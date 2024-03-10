from employee import *

class Chef :

    def __init__(self,nom=None) :
        self.__nom = nom
        self.__l_emp = []
        n = int(input("Entrer le nombre des Employées : "))
        for i in range(n) :
            self.__l_emp.append(Employee.ajouter())
             
    
    def ajouter() :
        nom = str(input("Nom du Chef : "))   
        chef = Chef(nom)
        return chef
    
    def afficher(self) :
        string = f"Le nom du chef est {self.__nom} \n"
        for i in self.__l_emp :
            string += i.afficher()
        return string
    
    def dict_to_json(self) :
        data = {}
        data["Nom Chef"] = self.__nom
        data["Employee"] = []
        for i in self.__l_emp :
            data["Employee"].append(i.dict_to_json())
        return data
    
    @property
    def nom(self) :
        return self.__nom
    @nom.setter
    def nom(self,valeur) :
        self.nom = valeur
