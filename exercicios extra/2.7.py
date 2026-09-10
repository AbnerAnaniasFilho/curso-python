# %%
frutas = {
    "Maçã": 1.50,
    "Banana": 2.75,
    "Uva": 1.90,
    "Pera": 1.25,
    "Laranja": 0.65,
    "Limão": 1.25,
    "Goiaba": 2.15,
    "Abacaxi": 3.20,
    "Jaca": 5.80
}

input_fruta = input("Digite o nome da fruta: ")
if input_fruta in frutas:
    preco = frutas[input_fruta]
    print(f"O preço da {input_fruta} é: R${preco:.2f}")
# %%
