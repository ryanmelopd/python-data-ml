import pandas as pd
import matplotlib.pyplot as plt


dataframe = pd.read_csv("01-python-dados/data/dados_jogos.csv")

nomes = dataframe["nome"].tolist()
precos = dataframe["preco"].tolist()

plt.bar(nomes, precos)

plt.title("Preço dos jogos")
plt.xlabel("Jogos")
plt.ylabel("Preço")

plt.show()