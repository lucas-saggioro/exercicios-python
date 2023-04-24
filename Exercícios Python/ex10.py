# Faça um programa que contenha um menu para as 4 operações básicas (Soma, Subtração, Produto e Divisão) mais a opção Sair.
# O programa deve simular uma calculadora e resolver a operação entre os 2 operandos (input do usuário).

while True:
    print("\nSelecione a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 5:
        break
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == 1:
        resultado = num1 + num2
        print("O resultado da soma é:", resultado)
    elif opcao == 2:
        resultado = num1 - num2
        print("O resultado da subtração é:", resultado)
    elif opcao == 3:
        resultado = num1 * num2
        print("O resultado da multiplicação é:", resultado)
    elif opcao == 4:
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    else:
        print("Opção inválida! Por favor, tente novamente.")