
# 1 2 3 4
# 1 2 4 3
# 1 4 2 3
# 1 4 3 2
# 1 3 4 2
# 1 3 2 4


# def loop(x) :
#     global Tab
#     for i in range(x) :
#         Tab.append(t.copy())
#         aide = t[i]
#         t[i] = t[i+1]
#         t[i+1] = aide
        

# t = []
# for _ in range(int(input("len : "))) :
#     # t.append(_+1)
#     t.append((input(f"Char {_+1} : ")))

# Tab = []
# for i in range(len(t)) :
#     loop(i)

# for k in Tab:
#     print(*k)

# -2 2
# -3 3
# -4 4


t = []
n = 4
for i4 in range(4) :
    for i3 in range(3) :
        for i2 in range(2) :
            t.append(2)
        t.append(3)
    t.append(4)
    t.append("||")

print(*t)

