def impares():
    impar = []
    for i in range(0, 5):
        lista=(int(input("Digite um número: ")))
        if (lista % 2 !=0):
            impar.append(lista)
    return impar
print(impares())