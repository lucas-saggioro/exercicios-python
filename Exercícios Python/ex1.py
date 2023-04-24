# Faça um programa que leia o nome, a idade, a altura, o peso e a nacionalidade do usuário e escreva essas informações na forma de um parágrafo de apresentação.

nome = input("Qual é o seu nome? ")
idade = input("Quantos anos você tem? ")
altura = input("Qual é a sua altura? ")
peso = input("Qual é o seu peso? ")
nacionalidade = input("Qual é a sua nacionalidade? ")

paragrafo = f"Olá, meu nome é {nome}, tenho {idade} anos, {altura} de altura, {peso} kg e sou {nacionalidade}."

print(paragrafo)