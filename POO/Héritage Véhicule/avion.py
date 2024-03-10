from vehicule import *

class Avion(Vehicule) :

    def __init__(self, vitesse: int = None, nbr_pas: int = None,nbr_moteur:int = None):
        super().__init__(vitesse, nbr_pas)
        self._nbr_moteur = nbr_moteur

    def saisir(self):
        super().saisir()
        self._nbr_moteur = int(input("Nombre de moteur : "))

    def affichage(self):
        string = super().affichage()
        return string + f"Nombre de moteur {self._nbr_moteur}"
