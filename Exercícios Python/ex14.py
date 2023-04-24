# Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

notas = []

for i in range(4):
    nota = float(input("Digite a {}ª nota: ".format(i+1)))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas: ", notas)
print("Média: ", media)