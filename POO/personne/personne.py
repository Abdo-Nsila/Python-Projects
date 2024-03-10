class Personne:
    # les propriete
    _nom = ""
    _prenom = ""
    _age = 0



# ----------------------------------    1    ----------------------------------

    def __init__(self,_nom=None  , _prenom=None , _age=None):
        self._nom = _nom
        self._prenom = _prenom
        self._age = _age


        
    def saisir(self) :
        self._nom = str(input('Enter first name : '))
        self._prenom = str(input('Enter last name : '))
        self._age = int(input('Enter your age : '))




    def descripToi(self):
        t = 'Nom:'+str(self._nom)+',   Prenom:'+str(self._prenom)+ ",   Age:"+str(self._age)
        return t




# ----------------------------------   2    ----------------------------------

    def retrait(self) :
        if self._age < 60 :
            age_avant_retrait = 60 - self._age
            return ("L'age avant retrait est : " , age_avant_retrait)
        else :
            return ("Vous etes en retrait")
    



# ---------------------------------   3    ----------------------------------


    def collection(self) :
        self._nom = str(input('Enter first name : '))
        self._prenom = str(input('Enter last name : '))
        self._age = int(input('Enter your age : '))

        info = [self._nom,self._prenom,self._age]
        return  info







