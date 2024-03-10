from personne import *
class Employee(Personne) :

    def __init__(self, nom: str = None, prenom: str = None, ville: str = None, age: int = None, salaire: int = None, societe : str = None):
        super().__init__(nom, prenom, ville, age)
        self._salaire = salaire
        self._societe = societe

    def saisir(self):
        super().saisir()
        self._salaire = int(input("Salaire : "))
        self._societe = str(input("Sociéte : "))

    def affichage(self):
        string =  super().affichage()
        return string + f" mon salaire est {self._salaire} mon sociéte {self._societe}"