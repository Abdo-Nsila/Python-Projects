# from itertools import product
# a = ["A" , "B" , "C"]
# b = [1 , 2 , 3]
# prod = product(a,b) #? Other parametre => prod = product(a,b,repeat=2)
# print(list(prod))


# from itertools import permutations
# a = [1,2,3,4]
# per = permutations(a) #? Other parametre => per = permutations(a,2) , short permutations of the original
# for i in list(per) :
#     print(*i)


# from itertools import combinations,combinations_with_replacement
# #! Combinations : give the sum of permutations  Not repeated
# a = [1,2,3,4]
# comb = combinations(a,2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))


# from itertools import accumulate
# import operator
# a = [1,2,3,4,5,6,7,8,9]
# accu = accumulate(a) #? Other parametre => accu = accumulate(a,operator.mul) 
# print(list(accu))


# from itertools import groupby
# def small_than_3(n) :
#     return n < 3
# l = [1,2,3,4]
# grp = groupby(l,key=lambda x : x<3) #* <==> grp = groupby(l,key=small_than_3)
# for key,value in grp :
#     print(key,list(value))

# personne = [{'name':'Abdellah','age':18,'city':'Marrakech'},{'name':'Omar','age':45,'city':'Dakhla'},{'name':'Youssef','age':9,'city':'Marrakech'}]
# grp1 = groupby(personne,key=lambda x: x['age']<=18)
# grp2 = groupby(personne,key=lambda x: x['city'])
# for key,value in grp1 :
#     print(key,list(value))
# for key,value in grp2 :
#     print(key,list(value))



# from itertools import count , cycle ,repeat
# a = [1,2,3,4]
# for i in count(10) :
#     print(i)
#     if i > 20 :
#         break
# for i in cycle(a) :
#     print(i)
# for i in repeat(a,4) :
#     print(i)
