# Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade. 

idade = input("Digite sua idade ")
idade = int(idade)
if idade < 18:
	print("Menor de idade")
if idade > 18:
	print ("Maior de idade")