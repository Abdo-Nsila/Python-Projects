def spin_words(sentence):
    l_sent = sentence.split(" ")
    l = [ i[::-1] if len(i) >= 5 else i  for i in l_sent ]
    sent = " ".join(l)
    return sent
print(spin_words("Abdellah abdo"))