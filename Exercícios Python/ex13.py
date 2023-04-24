# Ler uma lista de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(10):
    numero = float(input("Insira um número real: "))
    numeros.append(numero)

print("Lista na ordem inversa:")
for i in range(9, -1, -1):
    print(numeros[i])