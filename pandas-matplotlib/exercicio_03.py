import pandas as pd

dados = {
    "nome": ["Minecraft", "Terraria", "Elden Ring", "Hades"],
    "genero": ["Sandbox", "Sandbox", "RPG", "Roguelike"],
    "preco": [100, 40, 250, 90],
    "avaliacao": [9.2, 9.0, 9.5, 9.1]
}

dataframe = pd.DataFrame(dados)

print("\nJogos ordenados pelo preço, do maior para o menor:")
print(dataframe.sort_values(by="preco", ascending=False)[["nome", "preco"]])

print("\nJogos ordenados pelo preço, do menor para o maior:")
print(dataframe.sort_values(by="preco", ascending=True)[["nome", "preco"]])

print("\nJogos ordenados pela avaliação, do maior para o menor:")
print(dataframe.sort_values(by="avaliacao", ascending=False)[["nome", "avaliacao"]])


