


def valid_parethese(parenthese) :
    n = len(parenthese)
    if (n % 2) == 0 :
        # cond1 = (True if i=="(" else False for i in parenthese[:n//2])
        # cond2 = (True if i==")" else False for i in parenthese[n//2:])
        count1 = parenthese[:n//2].count("(")
        count2 = parenthese[n//2:].count(")")
        return True if (count1 == count2) and (count1 != 0 and count2 != 0) else False
    else :
        return False

print(valid_parethese(str(input("Enter a parethese : "))))
# count3 = parenthese.count("()")
# print(count3)
