# %%

txt = """Primal and naked
You dream of walls that hold us in prison (ah)
It's just a skull, least that's what they call it
And we're free to roam"""

nome_arquivo = "lyrics_02.txt"

with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)