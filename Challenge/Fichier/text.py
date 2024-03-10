
print("===================================================================================")
print("                           $$$$      LIST     $$$$                                 ")
print("===================================================================================")

f = open("D:\SCHOOL\Python\Challenge\Fichier\\text.txt","r")
t = []
name = []
prenom = []
age = []  
lignes = 5
for i in range(lignes) :
    a = f.readline()
    t.append(a.split(";"))
# print(t)
for j in range(len(t[i])) :
    for i in range(len(t)) :
        if j == 0 :
            name.append(t[i][j])
        elif j == 1 :
            prenom.append(t[i][j])
        elif j == 2 :
            age.append((t[i][j]).rstrip())

print(name)
print(prenom)
print(age)

print("\n"*5)



print("===================================================================================")
print("                           $$$$      DICT     $$$$                                 ")
print("===================================================================================")
# D1 = {}
# for j in range(1,(len(name))) :
#     D1["Nom"] = name[j]
#     D1["Prenom"] = prenom[j]
#     D1["Age"] = age[j]
#     print(D1)

# f.close()




# myFile = open("D:\SCHOOL\Python\Challenge\Fichier\\text.txt","r")
# list = myFile.readlines()
# keys = list[0].rstrip('\n').split(';')
# myDic = {}
# for i in range(1,len(list)):
#     for j in range(len(keys)):
#         myDic[keys[j]] = list[i].rstrip('\n').split(';')[j]
#     print(myDic)

f = open("D:\SCHOOL\Python\Challenge\Fichier\\text.txt","r")
list1 = []
D1 = {}
x = 0
list0 = f.readlines()
for i in range(len(list0)) :
    L = (list0[i].rstrip('\n').split(';')) 
    print(L)
    x += 1
    if x == 1 :
        D1["Nom"] = L[x]
    elif x == 2 :
        D1["Prenom"] = L[x]
    elif x == 3 :
        D1["Age"] = L[x]
    print(D1)
f.close()


