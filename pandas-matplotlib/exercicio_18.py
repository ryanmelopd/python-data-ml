import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("01-python-dados/data/dados_jogos.csv")

precos = dataframe["preco"].tolist()
avaliacoes = dataframe["avaliacao"].tolist()


plt.scatter(precos, avaliacoes)

plt.title("Preço x Avaliação dos Jogos")
plt.xlabel("Preço")
plt.ylabel("Avaliação")
plt.show()