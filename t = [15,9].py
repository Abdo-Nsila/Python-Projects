t = [[50,35],[40,25],[30,15],[20,5],[10,0]]
for j in range(2) :
    for i in range(len(t)-1 , -1 , -1) :
        if i == 0 :
            t[i][0] += 10
            t[i][1] += 5
        else :
            x , y = t[i-1]
            t[i][0] = x
            t[i][1] = y
    
print(t)


# class Snake :

#     def __init__(self , t=[]) :
#         self.__t = t
        
#     def move(self) :

#         for i in range(len(self.__t)) :
#             a = self.__t[i][0]
#             b = self.__t[i][1]
#             if i == 0 :
#                 self.__t[i][0] += 10
#                 self.__t[i][1] += 5
#             if i !=  len(self.__t)-1 :   
#                 self.__t[i+1][0] = a
#                 self.__t[i+1][1] = b
        
#         print(self.__t)


# object = Snake([[50,35],[40,25],[30,15],[20,5],[10,0]])
# object.move()

#                         <<< ---- After ---- :   >>>
# [[50,35],[40,25],[30,15],[20,5],[10,0]]



#                         <<< ---- Before ---- :  >>>
# ---------------------Changement :---------------
# t[i][0] += 10
# t[i][1] += 5
# And valeur of t[1] = t[0]   , t[2] = t[1] , t[3] = t[2] .......



# ---------The result I want to get :------
# [[60,40],[50,35],[40,25],[30,15],[20,5]]




