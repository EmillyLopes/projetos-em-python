r = "sim"
while r != " ":
    r = input("Deseja executar o programa? sim/nao\n")
    if r == "sim":
        d = float(input("Qual a distância percorrida (K)? "))
        t = float(input("Qual o tempo que levou para percorrer essa distância?(H) "))
        V = d / t
        print("A velocidade foi de:",V,"Km/H")
    else:
        exit()



