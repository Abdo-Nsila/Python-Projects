from personne import *
per1 = Personne()

object._name = "ok"
print(object._name)


# per1.saisir()
# print(per1.retrait())
# print(per1.descripToi())
# print(per1.collection())

tableau_info_personne = []
for i in range(2) :
    tableau_info_personne.append(per1.collection()) 
    print(tableau_info_personne)
    print(per1.descripToi())
    print(per1.retrait())