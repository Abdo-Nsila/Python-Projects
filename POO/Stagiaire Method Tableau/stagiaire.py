from colorama import Fore, Back, Style
class Stagiaire :

    listStg = []
    nbr_Stg = 0

    def __init__(self, nom=None, prenom=None, note=None) :
        self._nom = nom
        self._prenom = prenom
        self._note = note
        Stagiaire.nbr_Stg += 1

    def saisir(self) :
        self._nom = input(f"{Fore.MAGENTA}Nom : ")
        self._prenom = input(f"{Fore.MAGENTA}Prenom : ")
        self._note = float(input(f"{Fore.MAGENTA}Note : "))

    def afficher() :
        n = 0
        for i in Stagiaire.listStg :
            n += 1
            print(f"                                  {Fore.YELLOW}|----------Stagiaire {n}----------|{Fore.WHITE}\n")
            print(f"{Fore.CYAN}Nom:{i.nom}      Prenom:{i.prenom}       Note:{i.note}")

    @classmethod
    def ajouter(cls) :
        nom = input(f"{Fore.MAGENTA}Nom : ")
        prenom = input(f"{Fore.MAGENTA}Prenom : ")
        note = float(input(f"{Fore.MAGENTA}Note : "))
        stg = Stagiaire(nom,prenom,note)
        cls.listStg.append(stg)

    @classmethod
    def affiche_Super(cls) :
        for i in range(len(cls.listStg)) :
            if cls.listStg[i].note > 10 :
                print(f"{Fore.LIGHTGREEN_EX}{cls.listStg[i].nom}")

    @classmethod
    def calculer(cls) :
        sum = 0
        for i in range(len(cls.listStg)) :
            sum += cls.listStg[i].note
        print(f"{Fore.LIGHTGREEN_EX}La Moyenne : {sum / len(cls.listStg)}") 
                

    @classmethod
    def chercher(cls) :
        cher_Stg = input(f"{Fore.MAGENTA}Entrer le nom du Stagiaire : ")
        cond = False
        for i in range(len(cls.listStg)) :
            if cls.listStg[i].nom == cher_Stg :
                print(f"{Fore.GREEN}_____Le Stagiaire {cher_Stg} Exist_____")
                cond = True
        if cond == False :
            print(f"{Fore.RED}_____Le Stagiaire {cher_Stg} n' Exist pas !!!_____")
            

    @classmethod
    def modifier(cls) :
        cher_Stg = input(f"{Fore.MAGENTA}Entrer le nom du Stagiaire : ")
        cond = False
        for i in range(len(cls.listStg)) :
            if cls.listStg[i].nom == cher_Stg :
                note = float(input(f"{Fore.LIGHTMAGENTA_EX}Voici, Entrer la note : "))
                cls.listStg[i].note = note
                cond = True
        if cond == False :
            print(f"{Fore.RED}_____Le Stagiaire {cher_Stg} n' Exist pas !!!_____")


    @classmethod
    def supprimer(cls) :
        cher_Stg = input(f"{Fore.MAGENTA}Entrer le nom du Stagiaire : ")
        cond = False
        for i in range(len(cls.listStg)) :
            if cls.listStg[i].nom == cher_Stg :
                cond = True
                cls.listStg.pop(i)
                Stagiaire.nbr_Stg -= 1
                print(f"{Fore.GREEN}______Is Rmoved______")
            break
        if cond == False :
            print(f"{Fore.RED}Erreur_____Le Stagiaire {cher_Stg} n' Exist pas !!!_____")

    @classmethod
    def afficher_nbr_Stg(cls) :
        print(f"{Fore.GREEN}Nombre de Stagiaire : {cls.nbr_Stg}")



    @property
    def nom(self) :
        return self._nom
    @nom.setter
    def nom(self,valeur) :
        self._nom = valeur

    @property
    def prenom(self) :
        return self._prenom
    @prenom.setter
    def prenom(self,valeur) :
        self._prenom = valeur

    @property
    def note(self) :
        return self._note
    @note.setter
    def note(self,valeur) :
        self._note = valeur
    
