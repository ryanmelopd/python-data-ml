import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("pandas-matplotlib/data/dados_jogos.csv")

nomes = dataframe["nome"].tolist()
avaliacoes = dataframe["avaliacao"].tolist()


plt.plot(nomes, avaliacoes)

plt.title("Avaliações dos Jogos")
plt.xlabel("Jogos")
plt.ylabel("Avaliação")
plt.show()