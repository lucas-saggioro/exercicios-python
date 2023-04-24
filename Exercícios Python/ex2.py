# Faça um programa que receba o nome de 3 clientes e o valor que cada cliente pagou.
#O programa deve informar a quantidade de clientes que pagaram menos que a média dos valores e que pagaram mais que a média dos valores.

nome1 = input("Nome do cliente 1: ")
valor1 = float(input("Valor pago: "))

nome2 = input("Nome do cliente 2: ")
valor2 = float(input("Valor pago: "))

nome3 = input("Nome do cliente 3: ")
valor3 = float(input("Valor pago: "))

media = (valor1 + valor2 + valor3) / 3

if valor1 > media:
    print(f"{nome1}, pagou {valor1}, que é mais que a média dos valores")
else:
    print(f"{nome1}, pagou {valor1}, que é menos que a média dos valores")

if valor2 > media:
    print(f"{nome2}, pagou {valor2}, que é mais que a média dos valores")
else:
    print(f"{nome2}, pagou {valor2}, que é menos que a média dos valores")

if valor3 > media:
    print(f"{nome3}, pagou {valor3}, que é mais que a média dos valores")
else:
    print(f"{nome3}, pagou {valor3}, que é menos que a média dos valores")