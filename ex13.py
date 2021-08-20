c=0
n=0
q=0
for r in range(0,15) :
    r=int(input("Qual a sua opinião em relação ao filme: ótimo – 3, bom – 2, regular – 1.\n"))
    if r == 3 :
        c+=1
        print(c,"Pessoas reponderam ótimo")
    elif r == 2 :
        n+=1
        print(n,"Pessoas reponderam bom")
    elif r == 1 :
        q+=1
        print(q,"Pessoas reponderam regular")
