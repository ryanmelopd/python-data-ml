import pandas as pd

dados = {
    "nome": ["Minecraft", "Terraria", "Elden Ring", "Hades"],
    "genero": ["Sandbox", "Sandbox", "RPG", "Roguelike"],
    "preco": [100, 40, 250, 90],
    "avaliacao": [9.2, 9.0, 9.5, 9.1]
}

dataframe = pd.DataFrame(dados)

print("\nJogos que custam mais de 80:")
print(dataframe[dataframe["preco"] > 80])

print("\nJogos que custam menos de 100:")
print(dataframe[dataframe["preco"] < 100])

print("\nJogos que possuem avaliação maior que 9.1:")
print(dataframe[dataframe["avaliacao"] > 9.1])

print("\nNome dos jogos que custam mais de 80 e tem nota maior que 9.0:")
print(dataframe[
        (dataframe["preco"] > 80) &
        (dataframe["avaliacao"] > 9.0)]
        ["nome"])