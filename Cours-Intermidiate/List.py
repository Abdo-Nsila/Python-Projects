my_list = [5,10,-5,50,-20]

num = my_list.pop()
my_list.append(num)
new_list = sorted(my_list)   # my_list.reverse()
print(new_list)              # [-20, -5, 5, 10, 50]


list0 = [0] * 5              # [0,0,0,0,0]
list1 = [1,2,3,4,5,6,7,8,9]
l = list1[::-2]
print(l)

list0 = [2,8,4,6,9]
list1 = list0.copy()
list1.append("ADD")
print(list0)
print(list1)

list0 = [1,2,3,4,5,6,7,8,9]
list1 = [i*i for i in list0]
print(list1)

list0 = ["Hamza" , "Zoubair" , "Abdellah"]
if "Hamza" in list0 :
    print("Yes")
else :
    print("No")

list0 = ['a','p','p','l','e']
print(len(list0))
print(list0.count('p'))
print(list0.index("a"))
[print(f"{i}",end="_") for i in list0]
word = "".join(list0)
print("\n",word)


list0 = ["Abdellah" , 18 , "Morocco"]
name , age , country = list0
print(name)
print(age)
print(country)

list0 = [1,2,3,4,5]
i1 , *i2 , i3 = list0
print(i1)
print(i2)
print(i3)


import sys
my_list = [7 , 10 , "Hello" , 1337 , True]
my_tuple = (7 , 10 ,  "Hello" , 1337 , True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
