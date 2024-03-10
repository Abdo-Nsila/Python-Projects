from stagaire import *

while True:
    print("*"*20)
    print('Menu:')
    
    print('\t1- Ajout')
    print('\t2- Affiche')
    print('\t3- Valide satagaire')
    print('\t4- Moyenne')
    print('\t5- Cherche')
    print('\t6- Modifier un note')
    print('\t7- Supprime un stagaire')
    print('\t8- Nombre de stagaire')
    print('\t0- Quitte')
    choix = int(input('Enter ton choix:'))
    ### avic Match
    match choix:
        case 0:
            break
            
        case 1:
            Stagaire.ajoute()
            
        case 2:
            Stagaire.affiche()
            
        case 3:
            Stagaire.valideStagaire()
            
        case 4:
            Stagaire.moynneNote()
            
        case 5:
            Stagaire.cherche()
            
        case 6:
            Stagaire.modifierNote()
            
        case 7:
            Stagaire.supprimerStagaire()
            
        case 8:
            Stagaire.nombreOfStagaire()


    ### avec if else

    # if choix == 0:
    #     break
    # elif choix == 1:
    #     Stagaire.ajoute()
    # elif choix == 2:
    #     Stagaire.affiche()
    # elif choix == 3:
    #     Stagaire.valideStagaire()
    # elif choix == 4:
    #     Stagaire.moynneNote()
    # elif choix == 5:
    #     Stagaire.cherche()
    # elif choix == 6:
    #     Stagaire.modifierNote()
    # elif choix == 7:
    #     Stagaire.supprimerStagaire()
    # elif choix == 8:
    #     Stagaire.nombreOfStagaire()




