def double_letters(word) :
    for i in range(len(word)-1) :
        if word[i+1] == word[i] :
            return True
    return False