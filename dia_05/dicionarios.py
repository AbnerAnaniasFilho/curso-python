# %%

# pares de chava/valor

dados_abner = {
    "nome" : "Abner", 
    "sobrenome" : "Ananias",
    "filhos" : False,
    "formacao" : ["adm", "ads"],
    "cargos":[
        {"nome" : "estagiario", "empresa" : "publica"},
        {"nome" : "junior", "empresa" : "startup"},
        {"nome" : "pleno", "empresa" : "banco"},
        {"nome" : "senior", "empresa" : "fintech"},
    ]
}

# %%

print(dados_abner)
print(dados_abner["formacao"][-1])
print(dados_abner["cargos"][-1]["empresa"]) 

# %%

dados_abner["estado civil"] = "solteiro"

# %%

print("Chaves: ", dados_abner.keys())
print("Valores: ", dados_abner.values())
print("Itens: ", dados_abner.items())

# %%

for i in dados_abner:
    print(i, "->", dados_abner[i])

# %%

for chave, valor in dados_abner.items():
    print(chave, "->", valor)
