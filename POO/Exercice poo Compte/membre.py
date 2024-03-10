class Membre :
    def __init__(self,name:str) :
        self._name = name

    # La methode pour affichage de l'etet d'object
    def __str__(self) :
        return "Votre nom est : " + (str)(self._name)


    @property
    def name(self) :
        return self._name

    @name.setter
    def name(self,valeur) :
        self._name = valeur



        