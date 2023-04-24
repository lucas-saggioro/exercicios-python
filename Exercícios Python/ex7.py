# Faça um programa para que calcule a tabuada de x, onde x será um input do usuário.

num = int(input("Digite um número para ver sua tabuada: "))

for i in range(1, 11):
    print(num, "x", i, "=", num*i)