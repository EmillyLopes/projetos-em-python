produtos = ["Pão baguete","Torrada","Pão doce","Café","Tapioca", "Sonho"]
preco = [1.25, 4.30, 0.50, 1.30, 3.50, 2.35]
continua = True
i = 0
qtds = 0
desconto : float = 0
valor : float = 0
compras = []
qtd = []
print("""     
                                      PRODUTOS:
    ----------------------     ----------------------     ----------------------
   | Pão baguete - R$1,25 |   | Torrada - R$ 4,30    |   | Tapioca - R$3,50     |
   |       código =  0    |   |       código = 1     |   |       código = 4     |
   \----------------------/   \----------------------/   \----------------------/
   | Pão doce - R$0,50    |   | Café - R$1,30        |   | Sonho - R$ 2,35      |
   |       código = 2     |   |       código = 3     |   |       código = 5     |
   \----------------------/   \----------------------/   \----------------------/
    """)
while continua:
    compras.append(int(input("Qual o código do produto que deseja comprar? ")))
    qtd.insert(compras[i], int(input("Quantos produtos vc deseja comprar? ")))

    qtds += qtd[i]
    valor += preco[compras[i]]*qtd[i]
    while compras[i] < 0 or compras[i] >= 6:
        compras.pop(i)
        print("Produtos:")
        compras.append(int(input("Código errado ")))
    if qtds > 5:
        desconto = desconto-(desconto*1.0)
        print("Desconto de 10% aplicado pela compra de mais de 5 produtos!")

    i+=1

    continuar = input("Você deseja continuar? (S/N) ")
    while continuar != 'S' and continuar != 's' and continuar != 'N' and continuar != 'n':
        continuar = input("Você deseja continuar comprando? (S/N) ")
    if continuar == "N" or continuar == "n":
        break
while len(qtd) < 7:
    qtd.append(0)
print("--------------------------------------")
print("Produtos comprados: ")
print("--------------------")
for i in range(0, 6):
    print(produtos[i], ":",compras[i],qtd[i])
print("--------------------------------------")
print("Valor total:", '{0:.3}'.format(float(valor) / 3), "R$")
print("Valor com desconto:", '{0:.3}'.format(float(desconto) / 3), "R$")



