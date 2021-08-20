class Calculo:
    def __init__(self, salario):
        self.salario = salario


    def calcular_salario(self) :

        if self.salario < 300:
            return self.salario+(self.salario*0.45)
        elif 300 <= self.salario < 600:
            return self.salario+(self.salario*0.25)
        elif self.salario > 600:
            return self.salario+(self.salario*0.15)
