
class Date :

    def __init__(self,jour=None,mois=None,annee=None) :
        self.__jour = jour
        self.__mois = mois
        self.__annee = annee

    def fix(self,d,m,y) :
        self.__jour = d
        self.__mois = m
        self.__annee = y

    def afficher(self) :
        return f"{self.__jour}/{self.__mois}/{self.__annee}"