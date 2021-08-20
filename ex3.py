from time import sleep
for a in range(0,2) :
    A = float(input("Digite um número: "))
    B = float(input("Digite um número: "))
    opcao = int(input('''
    Selecione uma operação:\n1 | Média entre os números digitados\n2 | Diferença do maior pelo menor
3 | Produto entre os números digitados\n4 | Divisão do primeiro pelo segundo
    '''))

    if opcao == 1 :
        print("Resultado:",((A+B)/2))
    elif opcao == 2 :
        if A > B :
            print("Resultado:",A-B)
        if A < B :
            print("Resultado:",B-A)
    elif opcao == 3 :
        print("Resultado:",(A*B))
    elif opcao == 4 :
        print("Resultado:",(A/B))
    print("Deseja continuar?\n1-SIM\n2-NÃO\n")
    r=int(input())
    if r == 1 :
        print("c a r r e g a n d o . . .", end=' ',flush= True)
        sleep(0.5)
    elif r == 2:
        exit()