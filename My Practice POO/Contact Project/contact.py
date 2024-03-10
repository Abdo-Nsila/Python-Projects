from date import *
from colorama import Fore, Back, Style

class Contact() :

    def __init__(self, name=None, numTel=None) :
        self.__name = name
        self.__numTel = numTel
        self._dateCreation = Date.add()

    def add() :
        name = str(input("Contact Name : "))
        numTel = str(input("Contact Téléphone Number : "))
        obj = Contact(name,numTel)
        return obj
    
    def display(self):
        return f"       {Fore.BLUE}Contact Name : {Fore.RESET}{self.name}  ||  {Fore.CYAN}Contact Téléphone Number : {Fore.RESET}+212-{self.numTel}  ||  {self._dateCreation.display()}" 

    @property
    def name(self) :
        return self.__name
    @name.setter
    def name(self,valeur) :
        self.__name = valeur

    @property
    def numTel(self) :
        return self.__numTel
    @numTel.setter
    def numTel(self,valeur) :
        self.__numTel = valeur