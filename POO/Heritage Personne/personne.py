
class Personne :

    def __init__(self,nom:str=None,prenom:str=None,ville:str=None,age:int=None) :
        self._nom = nom
        self._prenom = prenom
        self._ville = ville
        self._age = age

    def saisir(self) :
        self._nom = str(input("Nom : "))
        self._prenom = str(input("Prenom : "))
        self._ville = str(input("Ville : "))
        self._age = int(input("Age : "))
        

    def affichage(self) :
        return f"Je m'appelle {self._nom} {self._prenom} j'ai {self._age} et j'abie à {self._ville}"



     