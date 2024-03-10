import csv
import json

# ! Question:[ 1 ]&[ 2 ]
f = open("clients.txt", "r", encoding="utf-8")
lignes = f.readlines()
[print(ligne) for ligne in lignes]
f.close()


# ! Question:[ 1 ]&[ 3 ]
f = open("produits.csv", "r")
lignes = csv.reader(f, delimiter=",")
[print(ligne) for ligne in lignes]
f.close()


# ! Question:[ 4 ]
f = open("commandes.json", "r")
x = json.loads(f.read())
# print(x)
f.close()

f = open("clients.txt", "r", encoding="utf-8")
lignes = f.readlines()
lignes = [ligne.rstrip().split(",") for ligne in lignes]
# print(lignes)
f.close()

f = open("produits.csv", "r")
ps = csv.DictReader(f, delimiter=",")
d = [p for p in ps]
# print(d)

for i in x:
    for j in lignes:
        if int(i["client_id"]) == int(j[0]):
            print("Information du client: ", j)
            print("Date du commande: ", i["date"])
            list_produit = []
            for h in i["products"]:
                for k in d:
                    if int(h["product_id"]) == int(k["id"]):
                        list_produit.append(k["produit"])
            print("Les produit commander: ", list_produit)
            print("-" * 70)


# ! Question:[ 5 ]
f = open("produits.csv", "r")
lignes = csv.DictReader(f, delimiter=",")
d = [ligne for ligne in lignes]
# print(d)

for i in x:
    total = 0
    for j in i["products"]:
        for k in d:
            if int(j["product_id"]) == int(k["id"]):
                total += float(k["prix"]) * float(j["quantity"])
    print(f"Le montant toale de la commande {i['id']} est: {total}")


# ! Question:[ 6 ]
for i in x:
    for j in i["products"]:
        for k in d:
            if int(j["product_id"]) == int(k["id"]):
                if int(j["quantity"]) > int(k["quantity"]):
                    print(
                        f"Erreur,la quantity commander est superieure de s'elle dans le stock =>  {int(j['quantity'])}>{int(k['quantity'])}"
                    )


# ! Question:[ 7 ]
from datetime import datetime

id = len(x) + 1
id_client = int("Entrer l'ID du client : ")
date = f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}"
nbr_produits = int(input("Entrer le nombre de produit que voulez vous commander :"))
l = []
for i in range(nbr_produits):
    product_id = int(input("Entrer l'ID du produit : "))
    quantity = int(input("Entrer la quantity du produit : "))
    l.append({"product_id": product_id, "quantity": quantity})

data = {"id": id, "client_id": id_client, "date": date, "products": l}

x.append(data)
fichier = open("commandes.json", "w")
fichier.write(json.dumps(x))
print("Vous avez ajouter une nouvelle commande avec success")
fichier.close()
