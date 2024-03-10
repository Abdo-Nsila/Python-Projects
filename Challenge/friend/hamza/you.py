t = [*range(10)]

# def square(num) :
#     return num ** 2
# TimeoutError
# # for n in t :
# #     print(square(n))
# print(*map(square,t))


from functools import reduce

t = [1,2,3]

def sum(n1,n2) :
    return n1 + n2
def square(num) :
    return num ** 2


print(reduce(lambda x,y : x ** 2),t)