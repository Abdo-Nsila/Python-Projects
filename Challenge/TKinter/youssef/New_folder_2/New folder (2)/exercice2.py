class Compte :
        nmcompte=0
        nom=""
        salaire=0
        def __init__(self,nmcompte=None,salaire=None,nom=None):
                self.nmcompte=nmcompte
                self.nom=nom
                self.salaire=salaire
        def saisir(self):
                self.nmcompte=input("entrer le numero de compte : ")
                self.nom=input("entrer votre nom :")
                self.salaire=int(input("entrer votre salaire : "))
        def crediter(self,montant=None):
                if (self.salaire==0):
                        return "tu peux pas faire cette operation car vous n'avez aucune salaire"
                elif(self.salaire!=0 and montant<self.salaire):
                        self.salaire=self.salaire - montant
                        return self.salaire
                elif (montant>self.salaire):
                        return 'votre solde est insuffisant , on a vider vottre compte , ton salaire est 0 '
        def debiter(self,montant=None):
                self.salaire=self.salaire+montant
                return self.salaire
        def affichage(self):
                print("votre nom : \n"  , self.nom,"\n","votre numéro de compte : \n",self.nmcompte," \n votre salaire : ")