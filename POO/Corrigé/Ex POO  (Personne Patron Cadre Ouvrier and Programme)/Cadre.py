from Personne import Peronne

class Cadre(Peronne):
    def __init__(self, nom: str = None, prenom: str = None, societe: str = None, num: int = None,indice:str=None):
        super().__init__(nom, prenom, societe, num)
        self.__indice = indice
        
    


    def saisir(self):
        super().saisir()
        self.__indice = str(input('Enter Indice: '))
        



    def afficahge(self):
        return super().getInfo() + f"\n\tIndice: {self.__indice}"
    


    def getSalaire(self):
        dic = {"E1":130000,"E2":150000,"E3":170000,"E4":200000}
        return f"Salair: {dic[self.__indice]} Dhs"

    
    def getInfo(self):
        return super().getInfo() + f"\n\t{self.getSalaire()}\n\tPost: Cadre"

    
