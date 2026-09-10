# %%
numero = int(input("Digite um número inteiro: "))
if numero / 3600 >= 1:
    horas = numero // 3600
    resto = numero % 3600
    minutos = resto // 60
    segundos = resto % 60
    print(f"{horas}:{minutos}:{segundos}")
elif numero / 60 >= 1:
    minutos = numero // 60
    segundos = numero % 60
    print(f"0:{minutos}:{segundos}")
else:
    print(f"0:0:{numero}")
# %%
