import time

print("Bem vindo a calculadora - TT")

opt = int(input("você deseja realizar qual operação abaixo? \n 1 - Soma \n 2 - Divisão \n 3 - Multiplicação \n 4 - Subtração \n 5 - Sair \n"))

if(opt != 5):
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o seu segundo numero: "))
else:
    exit

class Calculadora:

    def __init__(self,num1,num2):

        self.valor_a = num1
        self.valor_b = num2

    def soma (self):
        return self.valor_a + self.valor_b

    def divisao (self):

        if(self.valor_b != 0):
            return self.valor_a / self.valor_b
        else:
            print("Não existe divisão por zero!")

    def multiplicacao (self):
        return self.valor_a * self.valor_b

    def subtracao (self):
        return self.valor_a - self.valor_b

while opt != 5:

    if(opt == 1):
        calculadora = Calculadora(num1,num2)
        print("O resultado da soma é {:.2f}".format(calculadora.soma()))

    elif(opt == 2):
        calculadora = Calculadora(num1,num2)
        print("O resultado da divisão é {:.2f}".format(calculadora.divisao()))

    elif(opt == 3):
        calculadora = Calculadora(num1,num2)
        print("O resulta da multiplicação é {:.2f}".format(calculadora.multiplicacao()))

    elif(opt == 4):
        calculadora = Calculadora(num1,num2)
        print("O resultado da Subtração é {:.2f}".format(calculadora.subtracao()))

    else:
        print("Opção invalida! tente novamente.")
    
    opt2 = str(input("Deseja calcular novamente? ")).lower()

    if(opt2 == "sim"):
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o seu segundo numero: "))
        opt = int(input("você deseja realizar qual operação abaixo? \n 1 - Soma \n 2 - Divisão \n 3 - Multiplicação \n 4 - Subtração \n 5 - Sair \n"))

    else:
        opt = 5

print("Encerrando Sistema...")
time.sleep(3)
print("Sistema finalizado! Até a proxima!")
exit()
