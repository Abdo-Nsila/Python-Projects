class Personne :
    l_per = []

    def __init__(self,code=None,nom=None,prenom=None,age=None) :
        self.__code = code
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age

    def getInfo(obj) :
        print(f"Code:{obj.code}   Nom:{obj.nom}   Prenom:{obj.prenom}  Age:{obj.age}")

    def ajouter() :
        code = str(input("Code : "))
        nom = str(input("Nom : "))
        prenom = str(input("Prenom : "))
        age = int(input("Age : "))
        per = Personne(code,nom,prenom,age)
        Personne.l_per.append(per)

    def modifier(code,nom) :
        for i in Personne.l_per :
            if i.code == code and  i.nom == nom :
                i.nom = str(input("Entrer le Nom : "))

    def supprimer() :
        code = str(input("Entrer le code du Stagiaire a suupprimer : "))
        cond = False
        for i in Personne.l_per :
            if i.code == code :
                Personne.l_per.remove(i)
                print(f"{i.nom} {i.prenom}_____Removed____")
                cond = True
        if cond == False :
            print(f"Le code {code}_____Not_Exist____")

    def chercher() :
        code = str(input("Entrer le code du Stagiaire a chercher : "))
        cond = False
        for i in Personne.l_per :
            if i.code == code :
                print(f"{i.nom} {i.prenom}_____Exist____")
                cond = True
        if cond == False :
            print(f"Le code {code}_____Not_Exist____")
    
    def affichage() :
       for i in Personne.l_per :
            Personne.getInfo(i)

    def compter() :
        print(f"On a :  {len(Personne.l_per)} dans cette liste")
        
    def categorie() :
        for  i in Personne.l_per :
            if i.age < 18 :
                print(f"Categorie de {i.nom} : p")
            elif (i.age >= 19) and  (i.age <= 35) :
                print(f"Categorie de {i.nom} : j")
            else :
                print(f"Categorie de {i.nom} : g")


    @property
    def code(self) :
        return self.__code
    @code.setter
    def code(self,valeur) :
        self.__code = valeur

    @property
    def nom(self) :
        return self.__nom
    @nom.setter
    def nom(self,valeur) :
        self.__nom = valeur

    @property
    def prenom(self) :
        return self.__prenom
    @prenom.setter
    def prenom(self,valeur) :
        self.__prenom = valeur

    @property
    def age(self) :
        return self.__age
    @age.setter
    def age(self,valeur) :
        self.__age = valeur