

class Personne :
    def __init__(self,nom=None, prenom=None, societe=None, num=None) :
        self._nom = nom 
        self._prenom = prenom
        self._societe = societe
        self._num = num

    def saisir(self) :
        self._nom = str(input("Nom : "))
        self._prenom = str(input("Prenom : "))
        self._societe = str(input("Societe : "))
        self._num = str(input("Numero : "))

    def getInfo(self) :
        return f"Nom : {self._nom} Prenom : {self._prenom} La sociéte : {self._societe}"
