class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2

    def subtrair(self, num1, num2):
        return num1 - num2

    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        if num2 == 0:
            print("Aviso: Divisão por zero não é permitida.")
            return -1
        return num1 / num2


calc = Calculadora()

# Teste das operações
num1 = 10
num2 = 2

soma = calc.somar(num1, num2)
subtracao = calc.subtrair(num1, num2)
multiplicacao = calc.multiplicar(num1, num2)
divisao = calc.dividir(num1, num2)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
