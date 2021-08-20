r=[]
cont= 1
o= 0
b=0
re=0
for i in range(0,5):
    r.append(int(input("3–ótimo | 2–bom | 1-regular:\n")))
    if r[i] == 3:
        o = o+1
        print(o, "Pessoas reponderam ótimo")
    elif r[i] == 2:
        b = b + 1
        print(b, "Pessoas reponderam bom")
    elif r[i] == 1:
        re = re + 1
        print(re, "Pessoas responderam regular")