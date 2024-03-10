

def Ordre(t,cond):
    for i in range(len(t)):
        min = t[i]
        pos = i
        for j in range(i+1, len(t)):
            if min > t[j]:
                c = t[j]
                t[pos] = t[j]
                t[j] = min
                min = c
    if cond == False :
        print("||----------------------------||")
        print("")
        print("")
        for k in range(len(t)):
            print(t[k], end="")
        print("")
        print("")
        print("")
    elif cond == True :
        print("||----------------------------||")
        print("")
        print("")
        for k in range(len(t)):
            print(t[k], end=" ")
        print("")
        print("")
        print("")





def function_1():
    name = str(input("Entrer un Nom : "))
    cond = False
    t = []
    for k in range(len(name)):
        t.append(name[k])
    Ordre(t,cond)


def function_2():
    colone = int(input("Derminer la taille du tableau : "))
    cond = True
    t = []
    for i in range(colone):
        t.append(int(input("t["+str(i+1)+"] : ")))
    Ordre(t,cond)





while True:

    print("||------------------------------------------------------------------------------------------------------------||")
    print("||------------------------------------------------------------------------------------------------------------||")
    function = int(input("\n\nVoudrez vous mettre un mot en ordre alphabétique ! (Entrer 1) ! \n\nOu une liste des nombre ! (Entrer 2) ! \n\n          Quitter (Entrer 0) \n\n       Quelle choix voulait vous : "))
    print("")
    print("")
    
    if function == 1 :
        function_1()

    elif function == 2 :
        function_2()

    elif function == 0 :
        break

    else :
        print("):  ):  ):  ):    La commande ",function," est introuvable     ):  ):  ):  ):")
