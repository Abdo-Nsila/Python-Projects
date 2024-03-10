class Vehicule :

    def __init__(self,vitesse:int = None , nbr_pas:int = None) :
       self._vitesse = vitesse
       self._nbr_pas = nbr_pas

    def saisir(self) :
        self._vitesse = int(input("Vitesse : "))
        self._nbr_pas = int(input("Nombre de passagiers : "))

    def affichage(self) :
        return f"La vitesse {self._vitesse} MPH Nombre de passagiers {self._nbr_pas} "
