from personne import *
from ouvrier import *
from carde import *
from patron import *
p = Ouvrier()
Tab = []
for i in range(8) :
    p = Personne()
    Tab.append(p)

x = 0
for j in range(len(Tab)) :
    x += 1
    if x <= 1 :
        Tab[j] = Patron()
        Tab[j].saisir()
    elif x <= 3 :
        Tab[j] = Cadre()
        Tab[j].saisir()
    else :
        Tab[j] = Ouvrier()
        Tab[j].saisir()

x = 0
for j in range(len(Tab)) :
    x += 1
    if x <= 1 :
        print(Tab[j].getInfo())
        print(Tab[j].getSalaire())
        print("----------------------------------------------------------------------------------------")
    elif x <= 3 :
        print(Tab[j].getInfo())
        print(Tab[j].getSalaire())
        print("----------------------------------------------------------------------------------------")
    else :
        print(Tab[j].getInfo())
        print(Tab[j].getSalaire())
        print("----------------------------------------------------------------------------------------")



    


# # --------------------------------
# per = Personne()
# per.saisir()
# # --------------------------------
# p = Patron(per)
# Tab.append([p])
# # --------------------------------
# c1 = Cadre(per)
# c2 = Cadre(per)
# Tab.append([c1,c2])
# # --------------------------------
# ov1 = Ouvrier(per)
# ov2 = Ouvrier(per)
# ov3 = Ouvrier(per)
# ov4 = Ouvrier(per)
# Tab.append([ov1,ov2,ov3,ov4])
# # --------------------------------


# step = 0
# while step < 2 :
#     step += 1
#     for i in range(len(Tab)) :
#         for j in range(len(Tab[i])) :
#             if step == 1 :
#                 Tab[i][j].saisir()
#             elif step == 2 :
#                 print(Tab[i][j].getInfo())
#                 print(Tab[i][j].getSalaire())


