
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# 1 2 3 4 5 6 7 8 9 & - @ $ £ * % § ! # ^ µ / ~ = + -

word = str(input("Enter your text : "))
t = []
for r in range(len(word)) :
    t.append(word[r])
# print(t)
for i in range(len(t)) :
    if t[i] == "a" :
        t[i] = "1"
    elif t[i] == "b" :
        t[i] = "2"
    elif t[i] == "c" :
        t[i] = "3"
    elif t[i] == "d" :
        t[i] = "4"
    elif t[i] == "e" :
        t[i] = "5"
    elif t[i] == "f" :
        t[i] = "6"
    elif t[i] == "g" :
        t[i] = "7"
    elif t[i] == "h" :
        t[i] = "8"
    elif t[i] == "i" :
        t[i] = "9"
    elif t[i] == "j" :
        t[i] = "&"
    elif t[i] == "k" :
        t[i] = "-"    # a b c d e f g h i j k l m n o p q r s t u v w x y z
    elif t[i] == "l" :# 1 2 3 4 5 6 7 8 9 & - @ $ £ * % § ! # ^ µ / ~ = + -
        t[i] = "@"
    elif t[i] == "m" :
        t[i] = "$"
    elif t[i] == "n" :
        t[i] = "£"
    elif t[i] == "o" :
        t[i] = "*"
    elif t[i] == "p" :
        t[i] = "%"
    elif t[i] == "q" :
        t[i] = "§"
    elif t[i] == "r" :
        t[i] = "!"
    elif t[i] == "s" :
        t[i] = "#"
    elif t[i] == "t" :
        t[i] = "^"
    elif t[i] == "u" :
        t[i] = "µ"
    elif t[i] == "v" :
        t[i] = "/"
    elif t[i] == "w" :
        t[i] = "~"
    elif t[i] == "x" :
        t[i] = "="
    elif t[i] == "y" :
        t[i] = "+"
    elif t[i] == "z" :
        t[i] = "-"
    
for j in range(len(t)) :
    print(t[j],end="")
