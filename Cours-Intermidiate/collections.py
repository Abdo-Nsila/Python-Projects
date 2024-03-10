# from collections import Counter
# a = ["hello","world","hello","hello","world"] #? You can use a String
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.most_common()[1][0]) #! From this list ==> [('hello', 3), ('world', 2)]
# print(list(my_counter.elements()))


# from collections import namedtuple #? Used to Constracte a Tuple
# Cordonne = namedtuple('Cordonne','x,y,z')
# cord = Cordonne(1,-7,4)
# print(cord)
# print(cord.x , cord.y , cord.z) 
# [print(i,end=" ") for i in cord]
# print('')


# from collections import defaultdict
# dict0 = defaultdict(list)
# dict0["a"] = 1
# dict0["b"] = 2
# dict0["c"] = 3
# print(dict0["d"])

# from collections import deque
# d = deque()
# d.append(1)
# d.append(2)
# d.appendleft(3)
# d.extendleft(["A","B","C"])
# d.rotate(1) #? You can use this d.rotate(-1)
# print(d)
 
