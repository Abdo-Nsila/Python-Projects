
def sp_odd() :
    s = "abdo"
    s = "nsila"

    n = len(s)
    if n % 2 == 0 :
        pass
    else :
        s += "_"
    s = s.split(str,(n//2))    
    return s

# print(sp_odd())

s = "nsila"
print(s.split(""))

