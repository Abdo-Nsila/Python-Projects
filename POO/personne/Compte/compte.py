class Compte :
    _nbr_Compte = 0
    _nom_proprietaire = ""
    _salaire = 0

    def __init__(self,_nbr_Compte=None,_nom_Proprite=None,_salaire=None) :
        self._nbr_Compte = _nbr_Compte
        self._nom_Proprite = _nom_Proprite
        self._salaire = _salaire

    def saisir(self) :
        self._nbr_Compte = int(input("Entrer nombre du compte : "))
        self._nom_Proprite = str(input("Entrer votre nom :  "))
        self._salaire = int(input("Entrer votre salaire : "))


    def crediter(self) :
        nbr_Crediter = int(input("Enter l'argent a crediter : "))
        if self._salaire > nbr_Crediter :
            self._salaire -= nbr_Crediter
        else :
            self._salaire = 0
    
    def debiter(self) :
        nbr_Debiter = int(input("Enter l'argent a Debiter : "))
        self._salaire += nbr_Debiter

    
    def affichage(self) :
        return 'Numero du compte : ' + str(self._nbr_Compte) , 'Votre nom : ' , self._nom_Proprite , 'Votre salaire : ' + str(self._salaire)





