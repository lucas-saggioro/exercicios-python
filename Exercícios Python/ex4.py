#Faça um programa que receba 5 inputs do usuário, pode ser qualquer coisa (número inteiro, float ou string), mas cada input DEVE ser apenas de 1 único tipo de dados.
# Após receber imprima o valor do input bem como o tipo do mesmo.

#Exemplo:

#Valor 1: "1.5" - Float
#Valor 2: "Olá" - String
#Valor 3: "2" - Int

valores = []
tipos = []

for i in range(5):
    valor = input(f"Digite o valor {i+1}: ")
    try:
        valor = int(valor)
        tipo = "Int"
    except ValueError:
        try:
            valor = float(valor)
            tipo = "Float"
        except ValueError:
            tipo = "String"

    valores.append(valor)
    tipos.append(tipo)

    print(f"Valor {i+1}: {valor} - {tipo}")

print("\nValores digitados:")
for i in range(5):
    print(f"{i+1}: {valores[i]} - {tipos[i]}")