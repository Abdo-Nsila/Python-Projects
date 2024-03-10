
# DH --->  Dollar
def form_Dh_to_Dollar(money) :
    convert = money / 11
    return convert

# Dollar --> DH
def form_Dollar_to_Dh(money) :
    convert = money * 11
    return convert


while True :
    print("\n"*3)
    choix = int(input('From DH to $ (Enter 1) , From $ to DH (Enter 2) , Exit (Enter 3)  : '))


    if choix == 1 : 
        money = int(input('Enter money : '))
        print(form_Dh_to_Dollar(money))
    elif choix == 2 :
        money = int(input('Enter money : '))
        print(form_Dollar_to_Dh(money))
    elif choix == 3 :
        print("\n"*3)
        print('\n_________(:___/Goodbye Bro\\___(:__________\n')
        print("\n"*3)
        break
    else :
        print('Command is not found ):')

