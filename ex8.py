p=0
q=0
r=0
for n in range (0,10) :
    N= int(input("Digite sua idade:"))
    if N>0 and N <=15 :
        p+=1
        print("Tem",p," na 1ª Faixa etária")
    elif N >=16 and N <= 30:
        q+= 1
        print("Tem",q,"2ª Faixa etária")
    elif N >  30:
        r+= 1
        print("Tem",r,"3ª Faixa etária")
    else:
        exit()
