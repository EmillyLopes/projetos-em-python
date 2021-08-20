l=[]
n = 0

for i in range(0,4):
    l.append(float(input("Digite um número: ")))
    if l[i] < 0:
        n+=1
        print(n,"números negativos")
sposi = sum([i for i in l if i > 0])
print(sposi)