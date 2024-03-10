from personne import *
class Patron(Personne) :
    def __init__(self,nom=None, prenom=None, societe=None, num=None, ca = 0, pourcentage=0, salaire=0):
        super().__init__(nom,prenom,societe,num)
        self._nom = self._nom 
        self._prenom = self._prenom
        self._societe = self._societe
        self._num = self._num
        self._ca = ca
        self._pourcentage = pourcentage
        self._salaire = salaire

    def saisir(self):
        super().saisir()
        self._ca = int(input("Chiffre d'affere : "))
        self._pourcentage = int(input("pourcentage : "))

    def getSalaire(self) :
        self._salaire = self._ca * (self._pourcentage / 100)
        return self._salaire

    def getInfo(self):
        String = super().getInfo()
        return String + f" Salaire : {self.getSalaire()} poste ocuppe : Patron"