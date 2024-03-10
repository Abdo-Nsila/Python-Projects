def duplicate_Caracteres(chaine) :
    t1 = []
    for i in range(len(chaine)) :
        t1.append(chaine[i])

    t2 = t1
    t3 = []
    for j in range(len(t1)) :
        t3.append(t1[j])
        t3.append(t2[j])
    word = "".join(t3)
    return word

chaine = str(input("Enter a word : "))
print(duplicate_Caracteres(chaine))