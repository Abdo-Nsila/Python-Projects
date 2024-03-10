from entreprise import *

ent = Entreprise(str(input("Nom d'entreprise : ")))
print(ent.afficher())
ent.dict_to_json()