import random
while True :
    nbr_personne = int(input("Entrer le nombre de personne ( !!__le nombre doit etre pair et il doit etre valide a le composee__!!) : "))
    if (nbr_personne / 4) == int((nbr_personne / 4)) :
        break
Table = []
for i in range(nbr_personne) :
    Table.append(str(input("Entrer le nom du personne " + str(i+1) + " : ")))
t_Result = []
while len(Table) > 0 :
    t=[]
    nbr_personne = nbr_personne - 1 
    random_num = random.randint(0,nbr_personne)
    p1 = Table[random_num]
    Table.pop(random_num) 
    nbr_personne = nbr_personne - 1   
    random_num = random.randint(0,nbr_personne)
    p2 = Table[random_num]
    Table.pop(random_num)  
    t.append(p1)
    t.append(p2)
    t_Result.append(t)
print("||------------------------------------------------------||")
for h in range(len(t_Result)) :
        print("\n                     " , t_Result[h][0] , "Vs" , t_Result[h][1])
print("\n||------------------------------------------------------||")