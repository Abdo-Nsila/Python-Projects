def maskify(cc):
    cc = [i for i in cc]
    mcc = ["#"     if i<len(cc)-4      else cc[i]     for i in range(0,len(cc)) ]
    mcc = "".join(mcc)
    return mcc

print(maskify("Abdellah"))