# Faça um programa que enquanto for verdadeiro, peça 2 valores e uma operação e exiba o resultado.

while True:

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == '+':
        resultado = valor1 + valor2
    elif operacao == '-':
        resultado = valor1 - valor2
    elif operacao == '*':
        resultado = valor1 * valor2
    elif operacao == '/':
        resultado = valor1 / valor2
    else:
        print("Operação inválida.")
        continue

    print("O resultado da operação é:", resultado)
    
    continuar = input("Deseja continuar? (s/n)").lower()
    if continuar != 's':
        break