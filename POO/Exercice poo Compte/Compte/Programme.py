from compte import *
per = int(input("Enter number of personne : "))
table_Object_Of_Personne = []

for i in range(per) :
    cmp = Compte() 
    choix = int(input("Créditer Enter [1]   |    Débiter Enter [2] :   "))
    if choix == 1 :
        cmp.__nbr_Compte = int(input("Entrer numero du compte :"))
        cmp.__nom_Proprite = str(input("Entrer votre nom : "))
        cmp.__salaire = int(input("Entrer votre salaire : "))
        cmp.saisir()
        cmp.crediter()
        table_Object_Of_Personne.append(cmp)
    if choix == 2 :
        cmp.__nbr_Compte = int(input("Entrer numero du compte :"))
        cmp.__nom_Proprite = str(input("Entrer votre nom : "))
        cmp.__salaire = int(input("Entrer votre salaire : "))
        cmp.saisir()
        cmp.debiter()
        table_Object_Of_Personne.append(cmp)


print("              ||---------------------------------------------------||")
print("              ||             <| Liste Of Information |>            ||")
print("              ||---------------------------------------------------||")
print("\n"*5)
for j in range(per) :
    print("||------------------------------------------------------------------------------||")
    print("||                        Numero du personne" , str(j+1),                      "||")
    print("||",table_Object_Of_Personne[j].affichage(),"||")
    print("||______________________________________________________________________________||")

