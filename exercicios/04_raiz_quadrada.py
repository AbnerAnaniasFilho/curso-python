# Faça um programa que receba um número inteiro 
# e calcule sua raiz quadrada e exiba o resultado

numero = input("Entre com um número inteiro para calcular sua raiz quadrada: ")
numero = int(numero)

raiz = numero ** (1/2)
print("Raiz quadrada de", numero, "é:", raiz)