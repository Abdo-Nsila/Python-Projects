from rectangle import *
from cercle import *
from triangle import *
from carreau import * 

r = Rectangle()
cer = Cercle()
t = Triangle()
car = Carreau()
Tab = [r,cer,t,car]

for i in Tab :
    i.saisir()

for j in Tab :
    print(j.affichage())

