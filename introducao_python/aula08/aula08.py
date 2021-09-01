class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2
    
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicao(self):
        return self.a * self.b

    def divisao(self):
        if self.b != 0:
            return self.a / self.b
        return -1


if __name__ == '__main__':

    calculadora = Calculadora(5, 4)
    print(calculadora.soma())
    print(calculadora.subtracao())
