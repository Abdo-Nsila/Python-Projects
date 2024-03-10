class Compte :
    nbr_Compte = 0
    nom_Proprite = ""
    salaire = 0
    nbr_Crediter = 0
    nbr_Crediter = 0

    def __init__(self,nbr_Compte=None,nom_Proprite=None,salaire=None,nbr_Crediter=None,nbr_Debiter=None) :
        self.__nbr_Compte = nbr_Compte
        self.__nom_Proprite = nom_Proprite
        self.__salaire = salaire
        self.__nbr_Crediter = nbr_Crediter 
        self.__nbr_Debiter = nbr_Debiter

    def saisir(self) :
        self.__nbr_Compte = int(input("Entrer nombre du compte : "))
        self.__nom_Proprite = str(input("Entrer votre nom :  "))
        self.__salaire = int(input("Entrer votre salaire : "))

    @property
    def nbr_Compte(self) :
        return self.__nbr_Compte
    @property
    def nom_Proprite(self) :
        return self.__nom_Proprite
    @property
    def salaire(self) :
        return self.__salaire
    @property
    def nbr_Crediter(self) :
        return self.__nbr_Crediter
    @property
    def nbr_Debiter(self) :
        return self.__nbr_Debiter
    
    @nbr_Compte.setter
    def nbr_Compte(self,valeur) :
        self.__nbr_Compte = valeur

    @nom_Proprite.setter
    def nom_Proprite(self,valeur) :
        self.__nom_Proprite = valeur

    @salaire.setter
    def salaire(self,valeur) :
        self.__salaire = valeur

    @nbr_Crediter.setter
    def nbr_Crediter(self,valeur) :
        self.__nbr_Crediter = valeur

    @nbr_Debiter.setter
    def nbr_Debiter(self,valeur) :
        self.__nbr_Debiter = valeur


    def crediter(self) :
        self.__nbr_Crediter = int(input("Enter l'argent a crediter : "))
        if self.__salaire > self.__nbr_Crediter :
            self.__salaire -= self.__nbr_Crediter
        else :
            self.__salaire = 0
    
    def debiter(self) :
        self.__nbr_Debiter = int(input("Enter l'argent a Debiter : "))
        self.__salaire += self.__nbr_Debiter

    
    def affichage(self) :
        return 'Numero du compte : ' + str(self.__nbr_Compte) , 'Votre nom : ' , self.__nom_Proprite , 'Votre salaire : ' + str(self.__salaire)

    


