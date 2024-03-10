word = str(input("Enter a word : "))
t = []
x = 0
for i in range(len(word)) :
    if (word[i] == 'a') or (word[i] == 'i') or (word[i] == 'e') or (word[i] == 'i') or (word[i] == 'o') or(word[i] == 'u') or (word[i] == 'y') :
        x += 1
        t.append(word[i])
print("Numbers of voyels is : ",x, "\n Voyels in the word : ",end=" ")
for j in range(len(t)) :
    print(t[j],end=" ")

# word  = 'Abdellah'
# for i in range(len(word)) :
#     print(i)