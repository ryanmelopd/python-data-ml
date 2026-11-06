import pandas as pd

dados = {
    "nome": ["Minecraft", "Terraria", "Elden Ring", "Hades"],
    "genero": ["Sandbox", "Sandbox", "RPG", "Roguelike"],
    "preco": [100, 40, 250, 90],
    "avaliacao": [9.2, 9.0, 9.5, 9.1]
}

dataframe = pd.DataFrame(dados)

print("\nTabela completa:")
print(dataframe)

print("\nNomes:")
print(dataframe["nome"])

print("\nGenêros:")
print(dataframe["genero"])

print("\nPreços:")
print(dataframe["preco"])

print("\nAvaliações:")
print(dataframe["avaliacao"])

print("\nNomes e Preços:")
print(dataframe[["nome","preco"]])

print("\nNomes e avaliações:")
print(dataframe[["nome","avaliacao"]])

print("\nJogos com preço maior que 80:")
print(dataframe[dataframe["preco"] > 80])