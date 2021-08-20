f = 0
m=0
for i in range(0,3):
    sexo=int(input("Qual o sexo: 1-f/2-m  "))
    if sexo== 1:
        f = f+1
        print(f,"Pessoas do sexo feminino")
    else:
        m = m+1
        print(m, "Pessoas do sexo masculino")

