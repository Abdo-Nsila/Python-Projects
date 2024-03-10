from contact import *
from date import *
from colorama import Fore, Back, Style

class User :

    def __init__(self,name=str(input("User Name : ")),numTel=str(input("User Téléphone Number : "))) :
        self.__name = name
        self.__numTel = numTel
        self._dateCreation = Date.add()
        self._list_Contact = [Contact.add() for i in range(int(input("Enter number of Contact : ")))]

    def modify(self) :
        print(self.display())
        print(f"{Fore.YELLOW}__________________________________________[ Modify ]___________________________________________{Fore.RESET}")
        num = str(input("Enter Number of Contact : "))
        self._list_Contact[num-1].name = str(input("Enter new Name : "))
        self._list_Contact[num-1].numTel = str(input("Enter new Téléphone : "))
        print(f"{Fore.GREEN}________________[ Modify Success ]___________{Fore.RESET}\n")

    def remove(self) :
        print(self.display())
        print(f"{Fore.LIGHTRED_EX}__________________________________________[ Remove ]___________________________________________{Fore.RESET}")
        num = str(input("Enter Number of Contact : "))
        self._list_Contact.pop(num-1)
        print(f"{Fore.GREEN}________________[ Remove Success ]___________{Fore.RESET}\n")

    def search(self) :
        print(self.display())
        print(f"{Fore.CYAN}__________________________________________[ Search ]___________________________________________{Fore.RESET}")
        name = str(input("Contact Name : "))
        numTel = str(input("Contact Téléphone Number : "))
        cond = False
        for i in self._list_Contact :
            if i.name == name and i.numTel == numTel :
                cond = True
                return print(f"{Fore.GREEN}[ EXIST ]       {Fore.BLUE}Contact Name : {Fore.RESET}{i.name}  ||  {Fore.CYAN}Contact Téléphone Number : {Fore.RESET}{i.numTel}  ||  {i._dateCreation.display()}{Fore.GREEN}{Fore.RESET}\n")
        if cond == False :
            print(f"{Fore.LIGHTRED_EX}______[ Contact Not Found ! ]_____{Fore.RESET}\n")

    def display(self) :
        string = f"{Fore.RESET}||-------------------------------------------------------------------------------------------------------------------||\n"
        string += f"[Host]    {Fore.LIGHTRED_EX}User Name : {Fore.RESET}{self.name}   ||   {Fore.LIGHTRED_EX}User Téléphone Number : {Fore.RESET}+212-{self.numTel}  ||  {self._dateCreation.display()}"
        string += "||___________________________________________________________________________________________________________________||\n"
        n = 0
        for i in self._list_Contact :
            n += 1
            string += f"[{n}] " + i.display()
            string += "||___________________________________________________________________________________________________________________||\n"
        return string
    
    def count(self) :
        print(f"{Fore.YELLOW}Number of Contacts : {len(self._list_Contact)}")

    @property
    def name(self) :
        return self.__name
    @name.setter
    def name(self,valeur) :
        self.__name = valeur

    @property
    def numTel(self) :
        return self.__numTel
    @numTel.setter
    def numTel(self,valeur) :
        self.__numTel = valeur