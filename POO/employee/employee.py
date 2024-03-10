from date import *
class Employee :

    def __init__(self,codeEmp=None,nom=None,prenom=None,dateEmbouche=None) :
        self.__codeEmp = codeEmp
        self.__nom = nom
        self.__prenom = prenom
        self.dateEmbouche = Date()
        

        

    def lire(self) :
        self.__codeEmp = input("Entrer le code : ")
        self.__nom = input("Entrer votre nom : ")
        self.__prenom = input("Entrer votre prenom : ")
        d = int(input("jour : "))
        m = int(input("mois : "))
        y = int(input("Annee : ")) 
        self.dateEmbouche.fix(d,m,y)
        

    def afficher(self) :
        return f"CodeEmp:{self.__codeEmp}   Nom:{self.__nom}   Prenom:{self.__prenom} "
