l=[]
n = 0
p=[]
for i in range(0,4):
    l.append(float(input("Digite um número: ")))
    if l[i] < 0:
        n+=1
        print(n,"números negativos")
for o in range(len(l)):
    if o > 0:
        p[o]= sum(o)
sposi = sum([i for i in l if i > 0]