# *             *
#  *           *
#   *         *
#    *       *
#     *     *
#      *   *
#       * *
#      *   *
#     *     *
#    *       *
#   *         *
#  *           *
# *             *
#  *           * 
#   *         *
#    *       *
#     *     *
#      *   *
#       * *
#      *   *
#     *     *
#    *       * 
#   *         *
#  *           *
# *             *

ligne = int(input("Entrer le nombre de ligne : ")) 
r = int(input("Entrer le nombre de répétition : ")) 
# ligne = int(input("Entrer le nombre de ligne : "))    
ligne0 = ligne
ligne = ligne*2


c = (ligne0*2)+1
for i in range(r) :
    x = 1
    for j in range(ligne) :
        if j < ligne0 :
            x = x + 1
            c = c - 2
            print(" "*x + "*" +  " "*c + "*")
        elif j == ligne0  :
            c = 1
            for k in range(ligne0) :
                c = c + 2
                x = x - 1
                print(" "*x + "*" + " "*c + "*")

                # Ecrire un algorithme qui donne tot les possibiliter d'une chaine de nombre ou chaine de caractére :
                # Exemple :  123 132  213 231  312 321                      3 * 2 = 6
                # 1234 1243 1324 1342 1423 1432     2134 2143 2314 2341       4 * 6 = 24
