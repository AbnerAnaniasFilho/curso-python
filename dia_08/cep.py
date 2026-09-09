# %%

import requests # requisicoes na web
import json # tratar listas e dicionarios para arquivos json
from tqdm import tqdm
import pandas as pd

ceps = [
    "01001000",
    "20040002",
    "30110012",
    "70040010",
    "40026010",
    "50010000",
    "80010020",
    "60060150",
    "90010150",
    "69005010"
]

url = "https://viacep.com.br/ws/{cep}/json/"

dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())

dados

# %%

dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";")

# %%

with open("ceps.json", "w", encoding = 'utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii = False, indent = 4)

# %%