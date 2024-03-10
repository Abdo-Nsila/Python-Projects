from livre import *

l1 = Livre(titre="Titre",auteur="Ismaeel",prix=500,annee=2020)
l2 = Livre(l1)
print(l2.affichage())
