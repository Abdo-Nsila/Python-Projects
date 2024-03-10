def digital_root(n):
    while n > 9 :
        n = sum(int(i) for i in str(n))
    return n
            
print(digital_root(493193))
