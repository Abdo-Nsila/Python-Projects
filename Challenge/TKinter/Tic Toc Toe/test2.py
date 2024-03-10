# Tab = []
# for _ in range(int(input('Enter number of student : '))):
#     t = []
#     name = input()
#     t.append(name)
#     score = float(input())
#     t.append(score)
#     Tab.append(t)
Tab = [["Abdellah",90],["Ali",10],["Hamza",70],["Omar",70]]

for  i in range(len(Tab)) :
    if Tab[i][1] <= min0 :
        min0 = Tab[i][1]
min1 = 100
second_name = []
for  j in range(len(Tab)) :
    if Tab[j][1] <= min1 and Tab[j][1] != min0 :
        min1 = Tab[j][1]
        second_name.append(Tab[j][0])
for k in second_name :
    print(k)
# t = [5,8,21,44,75]
# t.sort()
# print(t)