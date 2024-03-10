
a = [1,2,3]
b = [4,5,6,7]

t = [[av , bv] for av , bv in zip(a,b)]
print(t)

t = [[i,av,bv] for i,(av,bv) in enumerate(zip(a,b))]  #! => (av,bv) is Important !
print(t)
