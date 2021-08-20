l=[]
n=1
c1=0
c2=0
c3=0
while n != 0 and n <=5:
    n+=1
    p=float(input("Qual o preço do produto: "))
    l.append(p)
    if p < 50 :
        c1+=1
    elif p >= 50 and p <=80:
        c2+=1
    elif p > 80:
        c3+=1
media= sum(l)/5
print("A média dos valores foi de:",media)
print("Quantidade de produtos com preço inferior a R$ 50,00: ",c1,"\nQuantidade de produtos com preço entre R$ 50,00 e 80,00: ",c2,"\nQuantidade de produtos com preço acima de R$ 80,00: ",c3)

