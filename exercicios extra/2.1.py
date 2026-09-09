# %%
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade < 18:
    print(f"{nome}, você não pode dirigir nem beber.")
elif idade >= 18 and idade <= 65:
    print(f"{nome}, bebida liberada! Só não vale dirigir!")
elif idade > 65:
    print(f"{nome}, beba com muita moderação!")
# %%
