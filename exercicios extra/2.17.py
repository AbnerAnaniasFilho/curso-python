# %%
palavra = input("Digite uma palavra: ")

palavra_formatada = palavra.strip().lower()

palavra_invertida = palavra_formatada[::-1]

if palavra_formatada == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo!")
else:
    print(f"A palavra '{palavra}' NÃO é um palíndromo.")
# %%
