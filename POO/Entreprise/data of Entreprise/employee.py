class Employee :

    def __init__(self,nom=None) :
        self.__nom = nom

    def ajouter() :
        nom = str(input("Entrer le nom d'Employée : "))
        emp = Employee(nom)
        return emp
    
    def afficher(self) :
        return f"Le nom d'Employée : {self.__nom} \n"
    
    def dict_to_json(self) :
        data = {}
        data["Nom Employee"] = self.__nom
        return data

    @property
    def nom(self) :
        return self.__nom
    @nom.setter
    def nom(self,valeur) :
        self.nom = valeur
        