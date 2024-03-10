from Personne import *
from Cadre import *
from Ouvrier import *
from Patron import *

TabPers = []
for i in range(0,8):
    p = Peronne()
    TabPers.append(p)

for i in range(0,len(TabPers)):
    if i == 0:
        TabPers[i] = Patron()
        TabPers[i].saisir()
    elif i==1 or i==2:
        TabPers[i] = Cadre()
        TabPers[i].saisir()
    else:
        TabPers[i] = Ouvrier()
        TabPers[i].saisir()
    print("______________________________")

for per in TabPers:
    print("+++++++++++++++++++++++++++++++")
    print(per.getInfo())