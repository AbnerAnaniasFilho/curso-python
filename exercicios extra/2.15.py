# %%

entrada = input("Digite os números separados por espaço (ex: 5 10 5 3): ")

lista_numeros = [int(numero) for numero in entrada.split()]

numero_procurado = int(input("Digite o número que deseja contar: "))

contagem = lista_numeros.count(numero_procurado)

print(f"O número {numero_procurado} aparece {contagem} vez(es) na lista.")
# %%
