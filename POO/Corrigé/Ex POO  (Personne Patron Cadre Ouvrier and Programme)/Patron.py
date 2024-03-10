from Personne import Peronne

class Patron(Peronne):
    def __init__(self, nom: str = None, prenom: str = None, societe: str = None, num: int = None, ca:float=None,persontage:float=None):
        super().__init__(nom, prenom, societe, num)
        self.__ca  =ca
        self.__persontage = persontage
        
    
    def saisir(self):
        super().saisir()
        self.__ca = float(input("Enter CA: "))
        self.__persontage = float(input('Enter Persontage: '))
        
    def affichage(self):
        return super().getInfo() + f'\n\tCA: {self.__ca}\n\tPersontage: {self.__persontage}'
    
    def getInfo(self):
        return super().getInfo() + f'\n\t{self.getSalaire()}\n\tPost: Patron'
    
    def getSalaire(self):
        return f"Salaire: {(self.__ca * self.__persontage)/100} Dhs"