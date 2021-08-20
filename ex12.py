
def maior (* núm):
    cont = maior = 0
    for valor in range(0,10):
        preco = int(input("Digite o preço do produto: "))
        print(f'{valor}')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
print(f'foram informados {cont} valores ao todo')
print(f' O Maior valor informado foi: {maior}')