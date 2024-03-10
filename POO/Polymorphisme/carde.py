from personne import *
class Cadre(Personne) :
    def __init__(self,nom=None, prenom=None, societe=None, num=None, indice=None, salaire=None):
        super().__init__(nom,prenom,societe,num)
        self._nom = self._nom 
        self._prenom = self._prenom
        self._societe = self._societe
        self._num = self._num
        self._indice = indice
        self._salaire = salaire

    def saisir(self):
        super().saisir()
        self._indice = str(input("Indice : "))

    def getSalaire(self) :
        if self._indice == "e1" :
            self._salaire = 38000
        elif self._indice == "e2" :
            self._salaire == 150000
        elif self._indice == "e3" :
            self._salaire = 170000
        elif self._indice == "e4" :
            self._salaire = 300000
        return self._salaire

    def getInfo(self):
        String = super().getInfo()
        return String + f" Salaire : {self.getSalaire()} poste ocuppe : Carde"