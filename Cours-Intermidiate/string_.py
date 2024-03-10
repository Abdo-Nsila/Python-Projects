# word = "    nsila   "
# word = word.strip() # => remove space
# print(word)

# words = "Hello World" 
# print(words.lower()) 
# print(words.upper()) 
# print(words.startswith("H"))   # => True
# print(words.endswith("World")) # => True

# print(words.find("d")) # return index
# print(words.count('o'))

# print(words.replace('World' , 'Friends'))

# from timeit import default_timer as timer
# word = ["a"] * 7
# start = timer()
# word = "".join(word)
# stop = timer()
# print(stop-start)
# print(word)

name = "Youssef"
age = 9
mark = 9.27
present = True
message = "{} _ {} _ {} _ {}".format(name,age,mark,present) 
print(message)

