class Rectangle() :
    largeur = 0
    langueur = 0


    def __init__(self,largeur = None,langueur = None,perimetre = None,surface = None) :
        self._largeur = largeur
        self._langueur = langueur
        self._perimetre = perimetre
        self._surface = surface
    
    def Saisir(self) :
        self._largeur = int(input("Entrer la largeur : "))
        self._langueur = int(input("Entrer  la langeur : "))

    def Perimetre(self) :
        self._perimetre = (self._largeur + self._langueur) * 2
        return ("Le Perimetre = " , self._perimetre)

    def Surface(self) :
        self._surface = self._largeur * self._langueur
        return ("Le Surface = " , self._surface)

    def Affichage(self) :
        return ('largeur est : ' , str(self._largeur)) , 'langeur est : ' , str(self._langueur)

    def deja_Creer(self) :
        return ('Perimetre est : ' , str(self._perimetre)) , 'Surface est : ' , str(self._surface)
