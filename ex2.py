
for time in range(0,2):
    time = int(input("Selecione um time:\n1- Flamengo\n2-Vasco\n"))
    gol = int(input("Quantos gols foram marcados?"))
    if time == 1:
        golf = gol
    elif time == 2:
        golv = gol
        if golv < golf :
            print("O time vencendor foi o Flamengo!!! Com um placar de :\nFlamengo=",golf,"VS Vasco=",golv)
        elif golv > golf :
            print("O time vencendor foi o Vasco!!! Com um placar de :\nFlamengo=",golf,"VS Vasco=",golv)
        else:
            print("Teve um empate! Placar de:\nFlamengo=",golf,"VS Vasco=",golv)



