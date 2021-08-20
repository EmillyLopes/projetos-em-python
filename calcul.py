class Calculadora:
    num: float
    num2: float
    oper: str

    def __init__(self, num, num2, oper):
        self.num = num
        self.num2 = num2
        self.oper = oper

    def calculadora(self):
        num = float(input("Digite um número: "))
        num2 = float(input("digite outro número: "))
        oper = input("Digite o operador (+,-,*,/): ")

        if (oper == "+"):
            return num + num2
        elif (oper == "-"):
            return num - num2
        elif (oper == "*"):
            return num * num2
        elif (oper == "/"):
            return num / num2
        else:
            print("Digite um valor")


print(Calculadora.calculadora(0))





