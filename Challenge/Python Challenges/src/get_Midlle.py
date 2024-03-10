
def midlle() :
    word = "abdo"
    word = "nsila"

    n = len(word)
    if n % 2 == 0 :
        med = (n // 2)
        return word[med-1] + word[med]
    else :
        med = ((n-1) // 2) + 1
        return word[med-1]
    
print(midlle())
