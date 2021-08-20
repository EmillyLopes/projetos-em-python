produtos = [" ", "Pão Baguete", "Pão Doce", "Tapioca", "Torrada", "Café", "Sonho"]
preco = [0, 1.5, 0.5, 3.5, 4.3, 1.3, 2.35]
soma=0
i=1
qtds=0
compras=[]
compras.append(0)
qtd=[]
qtd.append(0)
print("Produtos:")
print(" Pão Baguete - R$1.50 | Código: 1\n", "Pão Doce - R$0.50 | Código: 2\n", "Tapioca - R$3.50 | Código: 3\n", "Torrada - R$4.30 | Código: 4\n", "Café - R$1.30 | Código: 5\n", "Sonho- R$2.35 | Código: 6\n")

while True:
    compras.append(int(input("Qual o codigo do produto que você deseja comprar? ")))
    qtd.insert(compras[i], int(input("Qual a quantidade do produto que você deseja comprar? ")))
    
    qtds += qtd[i]
    while compras[i] < 1 or compras[i] > 6:
        compras.pop(i)
        print("Produtos:")
        print(" Pão Baguete - R$1.50 | Código: 1\n", "Pão Doce - R$0.50 | Código: 2\n", "Tapioca - R$3.50 | Código: 3\n", "Torrada - R$4.30 | Código: 4\n", "Café - R$1.30 | Código: 5\n", "Sonho- R$2.35 | Código: 6\n")
        compras.append(int(input("Código errado ")))

    soma += preco[compras[i]]*qtd[i]

    if qtds>5:
        soma*=0.9
        print("Você ganhou um desconto de 10% por ter mais de 5 produtos em sua compra!")
    
    i+=1

    deseja = input("Você deseja continuar comprando? (S/N) ")
    while deseja !='S' and deseja !='s' and deseja !='N' and deseja !='n':
        deseja = input("Você deseja continuar comprando? (S/N) ")

    if deseja == 'N' or deseja == 'n':
        break

while len(qtd) < 7:
    qtd.append(0)

print("Quantidades compradas:")
for x in range(1,7):
    print(produtos[x], ": ", qtd[x])

print ("Valor final: ",f'{soma:.3}',"R$")