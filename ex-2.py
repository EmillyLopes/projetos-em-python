gol = int(input("Quantos gols foram marcados?"))
time = int(input("Qual o time que marcou?\n1- Flamengo\n2-Vasco\n"))


class Gol:
    gol: int
    time: int


def marcagolflamengo(self, gol, time):
    if (time == 1):
        self.marcagolflamengo= time
        self.gol = gol
    return self.marcagolflamengo()


def marcagolvasco(self, gol, time):
    if (time == 2):
        self.marcagolvasco = time
        self.gol = gol
    return self.marcagolvasco


print(marcagolvasco(time=2,gol=int(input())))
print(marcagolflamengo(time=1,gol=int(input())))