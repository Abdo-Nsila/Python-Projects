class Stagaire(object):
    stagList = []
    def __init__(self,nom:str=None,prenom:str=None,note:float=None):
        self.__nom = nom
        self.__prenom = prenom
        self.__note = note
        

    #add stagaire obj to stagList
    def ajoute():
        print("_"*10,'ajoute un  Stagaire',"_"*10)
        
        nom = input('Enter nom:')
        prenom = input('Enter prenom:')
        note = float(input('Enter note:'))
        stg = Stagaire(nom,prenom,note)
        Stagaire.stagList.append(stg)
        print("done")
    

    #show all stagire name,lastname and note are in stagList
    def affiche():
        print("_"*10,'Affiche les Stagaires',"_"*10)
        for st in Stagaire.stagList:
            print("_"*20)
            print("Nom:",st.nom)
            print("Prenom:",st.prenom)
            print("Note:",st.note)
    

    #return list of stagiares
    def listStagaire():
        return Stagaire.stagList


    #remove stagire from stagList by his name
    def supprimerStagaire():
        print("_"*10,'suprimme un Stagaire',"_"*10)
        Nom = input('Enter nom:')
        suppUnStag = False
        for st in Stagaire.stagList:
            if st.nom == Nom:
                Stagaire.stagList.remove(st)
                suppUnStag = True
        if suppUnStag == False:
            print("stagaire n'exist pas!!!")
            
        else:
            print('Done')
    

    #return nombre of stagere in stagList
    def nombreOfStagaire():
        print("_"*10,'nomber of Stagaire',"_"*10)
        print(len(Stagaire.stagList))
    

    #return Moyanne of all stagiare note that in stagList
    def moynneNote():
        print("_"*10,'moyenne Note',"_"*10)
        sumNote = 0
        for st in Stagaire.stagList:
            sumNote += st.note
        print(f"Moyanne:",sumNote/len(Stagaire.stagList))


    #affiche un stagaire by his name
    def cherche():
        print("_"*10,'cherche',"_"*10)
        Nom = input('Enter nom:')
        found =False
        for st in Stagaire.stagList:
            if st.nom == Nom:
                print("_"*20)
                print("Nom:",st.nom)
                print("Prenom:",st.prenom)
                print("Note:",st.note)
                found = True
        if found == False:
            print("stagaire n'exist pas!!!")
            
        else:
            print('Done')
            
    

    #modfier Note of a stagaire by his name 
    def modifierNote():
        print("_"*10,'Modifier un note de stagaire',"_"*10)
        Nom = input('Enter nom:')
        Note = float(input('Enter note:'))
        modUnNote = False
        for st in Stagaire.stagList:
            if st.nom == Nom:
                st.note = Note
                modUnNote = True
        if modUnNote == False:
            print("stagaire n'exist pas!")
        else:
            print('Done')
    
    
    #affiche all stagire note >= 10
    def valideStagaire():
        n=0
        print("_"*10,'valide Stagaires',"_"*10)
        for st in Stagaire.stagList:
            if st.note >= 10:
                n += 1
                print("Nom:",st.nom)
                print("Prenom:",st.prenom)
                print("Note:",st.note)
                print("_"*20)
        
        print("nombre de satgaire valide est ",n,"/",len(Stagaire.stagList))


    #getters and setters
    #nom
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, valuer):
        self.__nom = valuer
    
    #prenom
    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, valuer):
        self.__prenom = valuer
    
    #note
    @property
    def note(self):
        return self.__note
    @note.setter
    def note(self, valuer):
        self.__note = valuer

