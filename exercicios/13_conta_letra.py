#Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Digite uma palavra: ")

count = 0

for letra in palavra:
    if letra == "a" or letra == "A":
        count += 1

print("A letra A aparece", count, "vezes")