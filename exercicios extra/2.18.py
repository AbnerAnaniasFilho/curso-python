# %%
frases_digitadas = {}

print("Digite suas frases. Pressione 'Enter' com a linha vazia para encerrar.\n")

while True:
    frase = input("Digite uma frase: ")
    
    if frase == "":
        break
    
    if frase in frases_digitadas:
        frases_digitadas[frase] += 1

    else:
        frases_digitadas[frase] = 1

print("\n--- Resumo das frases ---")

for f, quantidade in frases_digitadas.items():
    print(f"'{f}': {quantidade} vez(es)")
# %%
