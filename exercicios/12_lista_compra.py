# Faça um programa que verifique se o item que a pessoa escolheu para comprar 
# na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

produtos = ["laranja", "cerveja", "miojo", "carvão", "picanha"]

produto = input("Digite o produto que deseja comprar: ")

if produto in produtos:
    print("Produto está na lista!")
else:
    print("Produto não está na lista.")