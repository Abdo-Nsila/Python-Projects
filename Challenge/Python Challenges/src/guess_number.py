import random 
from colorama import Fore, Back, Style

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

def guess(x) :
    rand_num = random.randint(1,x)
    guess = 0
    while rand_num != guess :
        guess = int(input("Enter a number between (1 - 20) : "))
        if guess > rand_num :
            print(f"{Fore.RED} Sorry, is to hight !")
        elif guess < rand_num :
            print(f"{Fore.RED} Sorry, is to low !")
        print(Style.RESET_ALL)
    print(f"{Fore.GREEN} Congratulation the number is {rand_num}"+Style.RESET_ALL)

guess(20)