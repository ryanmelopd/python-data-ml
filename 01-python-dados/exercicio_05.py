import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_jogos.csv")

print("\nColuna de nomes:")
print(dataframe["nome"])

print("\nJogos com preço maior que 80:")
print(dataframe[dataframe["preco"] > 80]["nome"])

print("\nJogos ordenados pelo preço, do maior para o menor:")
print(dataframe.sort_values(by="preco", ascending=False)[["nome", "preco"]])

print("\nMédia de preços:")
print(dataframe["preco"].mean())

print("\nMédia de avaliações:")
print(dataframe["avaliacao"].mean())
