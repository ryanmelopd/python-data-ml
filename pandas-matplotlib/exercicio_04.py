import pandas as pd

dados = {
    "nome": ["Minecraft", "Terraria", "Elden Ring", "Hades"],
    "genero": ["Sandbox", "Sandbox", "RPG", "Roguelike"],
    "preco": [100, 40, 250, 90],
    "avaliacao": [9.2, 9.0, 9.5, 9.1]
}

dataframe = pd.DataFrame(dados)

print("\nMédia dos preços:")
print(dataframe["preco"].mean())

print("\nMaior avaliação:")
print(dataframe["avaliacao"].max())

print("\nMenor preço:")
print(dataframe["preco"].min())

print("\nSoma dos preços:")
print(dataframe["preco"].sum())

print("\nQuantidade de jogos:")
print(dataframe["nome"].count())

print("\nMédia das avaliações:")
print(dataframe["avaliacao"].mean())