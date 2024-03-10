class User :
    login = ""
    mot_passe = 0
    __conteur = 0
    def __init__(self , login=None , mot_passe=None) :
        self.__login = login
        self.__mot_passe = mot_passe
        User.__conteur += 1
        
    def tout_String(self) :
        return f"Votre login est : {self.__login} , Mot de passe : {self.__mot_passe}"

    def compter(self) :
        return f"Nombre d'utilisateur : {User.__conteur}"
    
    def saisir(self) :
        self.__login = str(input("Login : "))
        self.__mot_passe = str(input("Mot de passe : "))

    #----------------- Acceseur -------------------
    @property
    def login(self) :
        return self.__login
    #---------------- Mutateur --------------------
    @login.setter
    def login(self,valeur) :
        self.__login = valeur


    #----------------- Acceseur -------------------
    @property
    def mot_passe(self) :
        return self.__mot_passe
        #---------------- Mutateur --------------------
    @mot_passe.setter
    def mot_passe(self,valeur) :
        self.__mot_passe = valeur

    def __str__(self) :
        return "Votre login est : " +  (str)(self.__login) + " Mot de passe : " +  (str)(self.__mot_passe)

