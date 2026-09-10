# %%
posicao = int(input("Digite a posição na sequência de Fibonacci: "))
fibonacci = [0, 1]
for i in range(2, posicao + 1):
    proximo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)

print(f"O número na posição {posicao} da sequência de Fibonacci é: {fibonacci[posicao]}")

# %%
