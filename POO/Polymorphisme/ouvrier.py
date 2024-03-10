from datetime import *
from personne import *
class Ouvrier(Personne) :
    # date_Now = datetime.now()
    date_Now = 20
    _SMIG = 400000
    def __init__(self,nom=None, prenom=None, societe=None, num=None, dateEntree=None, age=0, salaire=0):
        super().__init__(nom,prenom,societe,num)
        self._nom = self._nom 
        self._prenom = self._prenom
        self._societe = self._societe
        self._num = self._num
        self._dateEntree = dateEntree
        self._age = age
        self._salaire = salaire
        

    def saisir(self):
        super().saisir()
        self._dateEntree = input("Enter date (day/mounth/year) :")
        self._dateEntree = datetime.strptime(self._dateEntree, "%d/%m/%Y")
        self._age = int(input("Age : "))

    def getSalaire(self) :
        # self._salaire = Ouvrier._SMIG + (self._age - 18) * 100 + ((Ouvrier.date_Now - self._dateEntree).days) * 150
        self._salaire = Ouvrier._SMIG + (self._age - 18) * 100 + ((Ouvrier.date_Now - self._dateEntree)) * 150
        if self._salaire > Ouvrier._SMIG :
            self._salaire = Ouvrier._SMIG * 2
        return self._salaire

    def getInfo(self):
        String = super().getInfo()
        return String + f" Salaire : {self.getSalaire()} poste ocuppe : Ouvrier"