import math
from colorama import Fore  

def progress_bar(progress,total) :

    percent = 100 * (progress / float(total))
    # bar = ('✔' * int(percent)) + ('-' * (100 - int(percent))) # window + $ => imoji
    if progress < (total/2) :
        bar = ('♦' * int(percent)) + ('-' * (100 - int(percent))) #! window + $ => imoji
        print(f"\r{Fore.LIGHTRED_EX}|{bar}| {percent:.2f}%",end="\r")    
    elif progress == total :
        bar = ('✔' * int(percent)) + ('-' * (100 - int(percent))) #! window + $ => imoji 
        print(f"\r{Fore.LIGHTGREEN_EX}|{bar}| {percent:.2f}%",end="\r")
    else :
        bar = ('¤' * int(percent)) + ('-' * (100 - int(percent))) #! window + $ => imoji
        print(f"\r{Fore.LIGHTYELLOW_EX}|{bar}| {percent:.2f}%",end="\r")

numbers = [i for i in range(100,7000)]
result = []

for index , num in enumerate(numbers) :  #* enumerate give index with value  => [0,577] [1,578] ...
    result.append(math.factorial(num))
    progress_bar(index + 1 , len(numbers))
print(f"{Fore.RESET}\n")


