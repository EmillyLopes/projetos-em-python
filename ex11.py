c = 0
n = 0
for r in range(0,15) :
    r=input("Você gosta de beterraba? Digite 1-SIM/2-NÃO\n")

    if r == "SIM" :
        c+=1
        print(c,"Pessoas reponderam SIM")
    elif r == "NÃO" :
        n+=1
        print(n,"Pessoas reponderam NÃO")