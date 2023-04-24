# Faça um programa que sorteie 10 números de 1 a 10, guarde-os em uma lista, e mostre o valor que foi sorteado mais vezes.

import random

numeros_sorteados = []

for i in range(10):
    numero = random.randint(1, 10)
    numeros_sorteados.append(numero)

print("Números sorteados:", numeros_sorteados)

contagem = {}
for numero in numeros_sorteados:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

numero_mais_frequente = None
frequencia_maxima = 0
for numero, frequencia in contagem.items():
    if frequencia > frequencia_maxima:
        numero_mais_frequente = numero
        frequencia_maxima = frequencia

print("Número sorteado mais vezes:", numero_mais_frequente)