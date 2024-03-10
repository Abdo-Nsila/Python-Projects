from exercice2 import *
print("-----------bienvenue dans notre prorammme----------")
nmbr=int(input("entrer le numero du person :"))
t=[]
for i in range (nmbr):
        print("----------------client n°",i+1,"-------------------")
        fon=int(input("choisir le type de fonction favorisé (1 pour le crediter / 2 pour le debiter ) : "))
        montant=int(input("entrer le montant : "))
        p1=Compte()
        p1.saisir()
        t.append(p1)
        print("-----------------------------------------------")
print("------------affichage d'information------------")
for j in range (nmbr):
        if (fon==1):
                t[j].affichage()
                print(t[j].crediter(montant))
        elif(fon==2):
                t[j].affichage()
                print(t[j].debiter(montant))

