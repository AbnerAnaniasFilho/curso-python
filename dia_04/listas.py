# %% 

idades = [10, 17, 25, 39, 33, 41, 57, 64, 67]
print(idades)

# %%

abner = ["Bel", "Ananias", 20, True, "Solteiro", 7777.77]
print(abner)

# %%

type(abner)

# %%

# idade
print(abner[2])

# %%

print("soma idades: ", sum(idades))

print("quantidade idades: ", len(idades))

print("média idades: ", sum(idades) / len(idades))

print("menor idade: ", min(idades))

print("maior idade: ", max(idades))

# %%

abner = ["Abner Ananias", 
         32,
         True, 
         "Solteiro",
         ["intern", "junior", "pleno", "senior", "head"],
         [1500, 4000, 7000, 10000, 15000],
         ["1", "2", "3"]]

print("dados do abner: ", len(abner))

print(abner[6][0])

num = abner[6]
primeiro_num = num[0]
print(primeiro_num)

# %%

tamanho = len(abner)

pos = tamanho - 1

num = abner[pos]

abner[pos] [len(num) - 1]
# %%

abner[-1][-1]

# %%
# [ start : stop ]
# primeiros 4 elementos
abner[0:4]

# %%

abner[4][3:5]

# %%

abner[4][-2:]

# %%

salarios = abner[5]
salarios[::2]

# [ start : stop : step ]