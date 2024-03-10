class Employee :

    def __init__(self,nom=None) :
        self.__nom = nom

    def ajouter() :
        nom = str(input("Entrer le nom d'Employée : "))
        emp = Employee(nom)
        return emp
    
    def afficher(self) :
        return f"Le nom d'Employée : {self.__nom} \n"

        