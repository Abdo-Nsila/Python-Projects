Tab = []
t_note = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    Tab.append([name,score])
    t_note.append(score)

t_note.sort()
print(f"La second Note = {t_note[1]}")
t_stu = []
for i in Tab :
    if i[1] == t_note[1] :
        t_stu.append(i[0])

t_stu.sort()
for j in t_stu :
    print(f"Student : {j}")

