# Faça um programa que leia e valide as seguintes informações:

# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# Use a função len(string) para saber o tamanho de um texto (número de caracteres).

while True:
    nome = input("Digite seu nome (maior que 3 caracteres): ")
    if len(nome) > 3:
        break
    else:
        print("O nome deve ter mais de 3 caracteres. Tente novamente.")

while True:
    idade = int(input("Digite sua idade (entre 0 e 150 anos): "))
    if idade >= 0 and idade <= 150:
        break
    else:
        print("A idade deve estar entre 0 e 150 anos. Tente novamente.")

while True:
    salario = float(input("Digite seu salário (maior que zero): "))
    if salario > 0:
        break
    else:
        print("O salário deve ser maior que zero. Tente novamente.")

while True:
    sexo = input("Digite seu sexo (f/m): ").lower()
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("O sexo deve ser 'f' ou 'm'. Tente novamente.")

while True:
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    else:
        print("O estado civil deve ser 's', 'c', 'v' ou 'd'. Tente novamente.")

print("Informações válidas registradas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estado_civil}")