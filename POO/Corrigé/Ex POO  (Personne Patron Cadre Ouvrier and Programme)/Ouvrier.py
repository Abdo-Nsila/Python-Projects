from Personne import Peronne
from datetime import *

class Ouvrier(Peronne):
    def __init__(self, nom: str = None, prenom: str = None, societe: str = None, num: int = None, DateE:date=None,SMIG:float=None,age:int=None):
        super().__init__(nom, prenom, societe, num)
        self.__SMIG = SMIG
        self.__age = age
        self.__dateE = DateE
        print(DateE)
        
    def saisir(self):
        super().saisir()
        self.__dateE = str(input('Enter date de enter (day/month/year): '))
        self.__SMIG = float(input('Enter SMIG: '))
        self.__age = int(input('Enter Age: '))
        
    #methode for get dateE enter - date now
    def diffDate(self,dateE):
        format = '%d/%m/%Y'
        today = date.today()
        Formattoday = today.strftime(format)
        date1 = datetime.strptime(Formattoday,format)
        date2 = datetime.strptime(dateE,format)
        diffDate = (date1 - date2).days
        return diffDate
        

        
        
    def affichage(self):
        return super().getInfo() + f'\n\tDate Enter: {self.__dateE}\n\tSMIG: {self.__SMIG}\n\tAge: {self.__age}'
    
    def getInfo(self):
        return super().getInfo() + f'\n\t{self.getSalaire()}\n\tPost: Ouvrier'
    
    def getSalaire(self):
        salair = self.__SMIG + (self.__age - 18)*100 + (self.diffDate(self.__dateE))*150
        if salair > self.__SMIG * 2 :
            return f"Salaire: {self.__SMIG * 2} Dhs"
        return f"Salaire: {salair} Dhs"
    
    
    
