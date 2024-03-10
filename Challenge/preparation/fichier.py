# f = open("test-1.txt","x",encoding='utf-8')
# f.write("Hello Abdo\n")
# f.close()

f = open("test-1.txt","a",encoding='utf-8')
f.write("Append Append youuuuuuuuuuuuuuu !\n")
f.write("Goo   Goo youuuuuuuuuuuuuuu !\n")
f.write("Nice    Nice   youuuuuuuuuuuuuuu !\n")
f.close()

f = open("test-1.txt","r",encoding='utf-8')
text = f.readlines()
f.close()
for i in range(len(text)) :
    print(text[i].replace("\n" , "OK"))
    print("----------",text[i][4:14],"----------")



