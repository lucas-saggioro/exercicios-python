# Faça um programa que simule as 4 operações básicas de uma calculadora.

def calculadora(operador, num1, num2):
    if operador == "+":
        return num1 + num2
    elif operador == "-":
        return num1 - num2
    elif operador == "*":
        return num1 * num2
    elif operador == "/":
        return num1 / num2
    else:
        print("Operação inválida!")

operacao = input("Selecione a operação desejada (+, -, *, /): ")

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))

resultado = calculadora(operacao, numero1, numero2)
print("O resultado da operação é:", resultado)