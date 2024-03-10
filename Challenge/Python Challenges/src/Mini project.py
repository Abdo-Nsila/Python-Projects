
#                                  List

# import csv #importer la bibliothèque csv
# fichier = open("fichier.csv", "r")
# lecteurCSV = csv.reader(fichier,delimiter=";") # Ouverture du lecteur CSV en lui fournissant le caractère séparateur (ici " ,")
# for ligne in lecteurCSV: # parcourir les lignes du fichier CSV
#     print(ligne) # afficher chaque ligne du fichier CSV
# fichier.close() #fermer le fichier CSV


#                                  Dict

import csv #importer la bibliothèque csv
fichier = open("fichier.csv", "r")
lecteurCSV = csv.DictReader(fichier,delimiter=";") # Ouverture du lecteur CSV en lui fournissant le caractère séparateur (ici " ,")
for ligne in lecteurCSV: # parcourir les lignes du fichier CSV
    print(ligne) # afficher chaque ligne du fichier CSV
fichier.close() #fermer le fichier CSV
