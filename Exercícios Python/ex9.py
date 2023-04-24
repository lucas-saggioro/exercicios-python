# Faça um programa que leia n valores fornecidos pelo usuário e calcule a soma de seus quadrados.

try:
    soma = 0

    while True:
        valor = input("Digite um valor númerico ou 'p' para parar de inserir:")

        if (valor != 'p'):
            soma += (float(valor) ** 2)
        else:
            break

    print(f'A soma do quadrado dos valores é {soma} ')

except ValueError:
    print('Você digitiou um valor incompatível com a operação a ser efetuada.')