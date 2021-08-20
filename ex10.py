c = 1
while c != 0 :
    print("----------------------------------------------")
    print("""1- Caderno - R$ 12.00 |2- Régua - R$ 2.50    |
3- Borracha - R$ 0.25 |4- Mochila - R$ 50.00 | """)
    print("----------------------------------------------")
    c = int(input("Digite o código do produto: "))
    q= int(input("Digite a quantidade adquirida: "))
    if c == 1 :
        print("\nCaderno - R$ 12.00 | O total pago será de :",q*12,"reais")
    elif c == 2 :
        print("\nRégua - R$ 2.50 | O total pago será de :", q*2.5,"reais")
    elif c == 3 :
        print("\nBorracha - R$ 0.25 | O total pago será de :",q*0.25,"reais")
    elif c == 4 :
        print("\nMochila - R$ 50.00 | O total pago será de :",q*50,"reais")