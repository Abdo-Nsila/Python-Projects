class Peronne(object):

    def __init__(self,nom:str=None,prenom:str=None,societe:str=None,num:int=None):
        self._nom = nom
        self._prenom =prenom
        self._societe = societe
        self._num = num
    
    def saisir(self):
        self._nom = str(input("Enter Nom: "))
        self._prenom = str(input('Enter prenom: '))
        self._societe = str(input('Enter societe : '))
        self._num = int(input('Enter num de telephone: '))

    def getInfo(self):
        return f"Info:\n\tNom: {self._nom}\n\tPrenom: {self._prenom}\n\tSociete: {self._societe}\n\tNum: {self._num}"

