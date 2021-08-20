preco = float(input("Digite o valor do produto:"))
#aumento
if preco < 50:
    novopreco = preco + (preco * 0.05)
elif preco >= 50 and  preco < 100:
    novopreco = preco + (preco * 0.10)
elif preco > 100:
    novopreco = preco + (preco * 0.15)

#classificação

if preco <= 80:
    print("O novo preço é :",novopreco,"reais, considerado um preço Barato")
elif preco > 80 and  preco <= 120:
    print("O novo preço é :",novopreco,"reais, considerado um preço Normal")
elif preco > 120 and  preco <= 200:
    print("O novo preço é :",novopreco,"reais, considerado um preço Caro")
elif preco > 200:
    print("O novo preço é :",novopreco,"reais, considerado um preço Muito Caro")
