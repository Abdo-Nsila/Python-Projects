from colorama import Fore, Back, Style
# colorama.init()

from date import *
from employee import *

em = Employee()


em.lire()
print(Fore.GREEN)
print(em.afficher())

print(Fore.WHITE)