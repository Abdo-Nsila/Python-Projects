from user import *
t = []
for i in range(4) :
    user = User()
    t.append(user)

for j in range(len(t)) :
    t[j].saisir()
    print(t[j].tout_String())
    
    cond = str(input("Voulez vos Modifier (Enter y)"))
    if cond == 'y' :
        val_log = str(input("Enter login :"))
        t[j].login_ = val_log
        val_passe = str(input("Enter mot_passe :"))
        t[j].mot_passe_ = val_passe
        print(t[j])
    print(t[j].compter())

