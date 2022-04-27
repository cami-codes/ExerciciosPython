#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
num1 = input("Digite o primeiro número ")
num1 = int(num1)
operador = input("Digite o operador ")
num2 = input("Digite o segundo número ")
num2 = int(num2)

if operador == "+":
	operacao = num1 + num2
print("Resultado ")
print(operacao)