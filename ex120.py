for valor in range(0,10):
    cont = maior = 0
    valor = int(input("Digite o preço do produto: "))
    print(f'{valor}')
    if cont == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor

print(f' O Maior valor informado foi: {maior}')