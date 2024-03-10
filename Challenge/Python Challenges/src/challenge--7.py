def add_dots(string) :
    string = list(string)
    add = ".".join(string)
    return add

def remove_dots(add) :
    y = add_dots(string).split(".")
    for i in range(len(y)) :
        print(y[i],end="")

string = str(input("Enter a word : "))
remove_dots(add_dots(string))

