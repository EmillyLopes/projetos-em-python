import desconto as desconto

class Produtos :
    prod={
        "Pão baguete" : 1.25,
        "Torrada" : 4.30,
        "Pão doce" : 0.50,
        "Café " : 1.30,
        "Tapioca" : 3.50,
        "Sonho" : 2.35
    }
    compras= []

    def valor_compras(self):
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
        cod= int(input("digite o código do produto: "))
        qtd= int(input("Quantos produtos irá comprar?"))
        valor= cod*qtd
        compras.append(cod,qtd)
        return valor

    if qtd >= 5:
        desconto= desconto-(desconto*1.0)
        print("Desconto de 10% aplicado pela compra de mais de 5 produtos!")

    continuar = input("Você deseja continuar comprando? S/N) ")

    while continuar == 'S' or 'Sim' or 'SIM':
        cod = int(input("digite o código do produto: "))
        qtd = int(input("Quantos produtos irá comprar?"))