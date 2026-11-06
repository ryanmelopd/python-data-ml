import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_jogos.csv")

print("\nPreço médio de cada gênero:")
print(dataframe.groupby("genero")["preco"].mean())

print("\nAvaliação média de cada gênero:")
print(dataframe.groupby("genero")["avaliacao"].mean())

print("\nContagem de jogos de cada gênero:")
print(dataframe.groupby("genero")["nome"].count())

print("\nPreço médio dos jogos de RPG:")
print(dataframe.groupby("genero")["preco"].mean()["RPG"])

