# %%
import pandas as pd
import requests

url = "https://api.brawlstars.com/v1/brawlers"

headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9."
"eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImI1MWU0ZjFiLTExMjAtNDU4YS05MzQzLWM4NWE5NGE1ODM5YiIsImlhdCI6MTc4O"
"DkxMjc3MCwic3ViIjoiZGV2ZWxvcGVyLzk3NWQyN2IyLTQzMzAtNDhkYy05NmFmLWM2MzI4NTRjODI4MiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGl"
"lciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTc3LjEwMi45Ni4xOTMiXSwidHlwZSI6ImNsaWVudCJ9XX0.T25HP65cDEj-S8"
"d-7U6M0owP_ktDSt5TG2X02uwODZcBdrR07frrIBy0CvFPF4k3nln0k3nttBCKfjNrEYEcWw"}

resposta = requests.get(url, headers=headers)

print("Status Code:", resposta.status_code)

dados_json = resposta.json()
df = pd.DataFrame(dados_json["items"])
df.to_csv("brawlers.csv", sep=";", index=False)
# %%
