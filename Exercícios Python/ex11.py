# Peça 5 valores de qualquer tipo para o usuário, guarde na em uma lista, em seguida imprima-os.

valores = []
for i in range(5):
    valor = input("Digite um valor: ")
    valores.append(valor)

print("Os valores digitados foram:")
for valor in valores:
    print(valor)