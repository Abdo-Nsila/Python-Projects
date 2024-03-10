from comp import *

print("Hala Hala l mgharba Sbo3a w Rjala ....  Diro Diro Nyya Ynsrna L3ali Ta3ala")
print
per = int(input("Enter number of personne : "))
table_Object_Of_Personne = []

for i in range(per) :
    cmp = Compte() 
    choix = int(input("Créditer Enter [1]   |    Débiter Enter [2] :   "))
    if choix == 1 :
        cmp.saisir()
        cmp.crediter()
        table_Object_Of_Personne.append(cmp)
    if choix == 2 :
        cmp.saisir()
        cmp.debiter()
        table_Object_Of_Personne.append(cmp)


print("              ||---------------------------------------------------||")
print("              ||             <| Liste Of Information |>            ||")
print("              ||---------------------------------------------------||")
print("\n"*5)
for j in range(per) :
    print("||------------------------------------------------------------------------------||")
    print("||                        Numero du personne" , str(j+1)                       ,"||")
    print("||",table_Object_Of_Personne[j].affichage(),"||")
    print("||______________________________________________________________________________||")

