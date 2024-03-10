
def comp(array1, array2):




    for i in array1 :
        cond = False
        for j in array2 :
            if i**2 == j :
                cond = True
        if cond == False :
            return False  
    return True

print(comp([121, 144, 19, 161, 19, 144, 19, 11],[11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]))