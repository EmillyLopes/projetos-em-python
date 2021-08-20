nome= ' '
salario = 1
maior_salario = 0.0
nome_maior = ''
menor_salario = 0.0
nome_menor = ""
pessoas_1500 = 0
n_filhos= 0
pessoas=0

while salario > 0:
    print('---------------------------------------------------------------------------------')
    nome = input("Digite o nome: ")
    pessoas+=1
    salario = float(input("Digite o salário: "))
    if salario < 0:
        break

    if salario > maior_salario:
        maior_salario = salario
        nome_maior = nome

    elif salario < menor_salario:
        menor_salario = salario
        nome_menor = nome

    media_salario = salario / pessoas

    if salario <= 1500:
        pessoas_1500 += 1
        porcentagem = (pessoas_1500/pessoas)*100

    n_filhos = int(input("Digite quantos filhos tem: "))
    media_filhos = n_filhos/pessoas
print('---------------------------------------------------------------------------------')
print("A media do salario da população: ",media_salario)
print("A media do números de filhos é de: ",media_filhos)
print(f"O maior salario foi de: {nome_maior},{maior_salario} R$ e o menor salario foi de: {nome_menor}, {menor_salario} R$")
print("O percentual de pessoas com o salário até R$1500,00 é: ",porcentagem)'%'
print('---------------------------------------------------------------------------------')