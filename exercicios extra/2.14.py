# %%

lista_numeros = [123, 435, 987, 1984, 2, 19, 423, -178, 320]
maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

for i in lista_numeros:
    if i == maior_valor:
        print(f"O maior valor da lista esta na posição {lista_numeros.index(maior_valor)} e é: {maior_valor}")
    elif i == menor_valor:
        print(f"O menor valor da lista esta na posição {lista_numeros.index(menor_valor)} e é: {menor_valor}")

# %%
