from abc import ABC, abstractmethod


class Animal(ABC) :

    def __init__(self, nom=None, voice=None) :
        super().__init__()
        self.__nom = nom
        self.__voice = voice

    @abstractmethod
    def saisir(self) :
        pass

    @abstractmethod
    def voiceAnimal(self) :
        pass




class Dog(Animal) :

    def __init__(self, nom=None, voice=None):
        super().__init__(nom, voice)

    def saisir(self):
        super().saisir()
        self.nom = str(input("Entre votre nom :"))
        self.voice = str(input("Entre votre voice :"))

    def voiceAnimal(self):
        super().voiceAnimal()
        return f"Nom:{self.nom}, Voice:{self.voice}"
    
    @property
    def nom(self) :
        return self.__nom
    @nom.setter
    def nom(self, valeur) :
        self.__nom = valeur

    @property
    def voice(self) :
        return self.__voice
    @voice.setter
    def voice(self, valeur) :
        self.__voice = valeur


# ani1 = Dog()
# ani1.saisir()
# print(ani1.voiceAnimal())




















class Personne(ABC) :

    def __init__(self, nom=None, salaire=0) :
        self.__nom = nom
        self.__salaire = salaire

    def saisir(self) :
        self.nom = str(input("Entre votre nom :"))
        self.salaire = float(input("Entre votre salaire :"))

    def affichage(self) :
        string = f"Votre Nom:{self.nom}, Votre salaire:{self.salaire}"
        return string
    
    @property
    def nom(self) :
        return self.__nom
    @nom.setter
    def nom(self, valeur) :
        self.__nom = valeur

    @property
    def salaire(self) :
        return self.__salaire
    @salaire.setter
    def salaire(self, valeur) :
        self.__salaire = valeur



class Employee(Personne) :

    def __init__(self, nom=None, salaire=0, age=0):
        super().__init__(nom, salaire)
        self.__age = age

    def saisir(self):
        super().saisir()
        self.age = int(input("Entre votre age :"))

    def affichage(self):
        return super().affichage() + f", Votre Age:{self.age}"

    @property
    def age(self) :
        return self.__age
    @age.setter
    def age(self, valeur) :
        self.__age = valeur



# obj1 = Employee()
# obj1.saisir()
# print(obj1.affichage())

















class Personne:
    def __init__(self,nom):
        self.nom=nom
     
    def affiche(self):
        print("je suis une personne")
 
class Etudiant(Personne):
    def __init__(self,nom,cne):
        super().__init__(nom)  
        self.cne=cne
     
    def affiche(self):
        print("je suis un etudiant")
 
class Professeur(Personne):
    def __init__(self,nom,ppr):
        super().__init__(nom)  
        self.ppr=ppr
     
    def affiche(self):
        print("je suis un professeur")
 



etd=Etudiant('Kayouh',123444)
prf=Professeur('ESSADDOUKI',123123123)

 
etd.affiche()
prf.affiche()