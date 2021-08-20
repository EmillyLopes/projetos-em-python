salario= float(input("Digite o seu salário:"))

if salario < 300:
    salario= salario + (salario * 0.45)
elif 300 <= salario < 600:
    salario= salario + (salario * 0.25)
elif salario > 600:
    salario= salario + (salario * 0.15)

print("O Salário reajustado é:",salario, "reais")