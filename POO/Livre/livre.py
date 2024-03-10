class Livre :

    nbr_livre = 0

    def __init__(self,obj=None,titre=None,auteur=None,prix=None,annee=None) :
        if obj is not None :
            self.__titre = obj.__titre
            self.__auteur = obj.__auteur
            self.__prix = obj.__prix
            self.__annee = obj.__annee
        else :
            self.__titre = titre
            self.__auteur = auteur
            self.__prix = prix
            self.__annee = annee
        Livre.nbr_livre += 1


    def affichage(self) :
        return f"Titre : {self.__titre} Auteur : {self.__auteur} Prix : {self.__prix} Année : {self.__annee}"
    

    @property
    def titre(self) :
        return self.__titre
    @titre.setter
    def titre(self,valeur) :
        self.__titre = valeur

    @property
    def auteur(self) :
        return self.__auteur
    @auteur.setter
    def auteur(self,valeur) :
        self.__auteur = valeur

    @property
    def prix(self) :
        return self.__prix
    @prix.setter
    def prix(self,valeur) :
        self.__prix = valeur

    @property
    def annee(self) :
        return self.__annee
    @annee.setter
    def annee(self,valeur) :
        self.__annee = valeur
     

