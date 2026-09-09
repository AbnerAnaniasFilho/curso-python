# %%
import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

chave_api_brawl_stars = os.getenv("CHAVE_API_BRAWL_STARS")

url = "https://api.brawlstars.com/v1/brawlers"

headers = {
    "Authorization": f"Bearer {chave_api_brawl_stars}"
}

resposta = requests.get(url, headers=headers)

print("Status Code:", resposta.status_code)

# Verifica se a requisição foi um sucesso (código 200)
if resposta.status_code == 200:
    dados_json = resposta.json()
    df = pd.DataFrame(dados_json["items"])
    df.to_csv("brawlers.csv", sep=";", index=False)
    print("Sucesso! Arquivo brawlers.csv foi criado.")
else:
    # Se falhar, imprime a mensagem de erro que o servidor enviou
    print("A API recusou a conexão. Detalhes do erro:")
    print(resposta.text)# %%

# %%
