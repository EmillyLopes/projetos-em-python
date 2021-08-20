r=[]
cont= 1
o= 0
b=0
re=0
while cont != 0 and cont<= 5 :
    cont+=1
    r.append(int(input("3–ótimo | 2–bom | 1-regular:\n")))
if r[cont] == 3:
    o = o+1
    print(o, "Pessoas reponderam ótimo")
elif r[cont] == 2:
    b = b + 1
    print(b, "Pessoas reponderam bom")
elif r[cont] == 1:
    re = re + 1
    print(re, "Pessoas responderam regular")
