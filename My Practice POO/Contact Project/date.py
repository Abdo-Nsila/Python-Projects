import datetime
from colorama import Fore, Back, Style

class Date :

    def __init__(self,dateCreation=None) :
        self.__dateCreation = dateCreation

    def add() :
        dateCreation = datetime.date.today()
        obj = Date(dateCreation)
        return obj
    
    def display(self) :
        return f"{Fore.LIGHTGREEN_EX}Creation Date : {Fore.RESET}{self.dateCreation}   \n"
    
    @property
    def dateCreation(self) :
        return self.__dateCreation
    @dateCreation.setter
    def dateCreation(self,valeur) :
        self.__dateCreation = valeur
