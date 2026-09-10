# %%
notas = [float(input(f"Digite a {i+1}ª nota: ")) for i in range(4)]

media = sum(notas) / len(notas)
menor = min(notas)
maior = max(notas)

print(f"\nMédia: {media:.1f}")
print(f"Menor: {menor:.1f}")
print(f"Maior: {maior:.1f}")
# %%
