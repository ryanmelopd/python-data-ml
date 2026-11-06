import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("01-python-dados/data/dados_vendas.csv")

dataframe["total_vendas"] = dataframe["preco"] * dataframe["quantidade"]

vendas_por_categoria = dataframe.groupby("categoria")["total_vendas"].sum()

categorias = vendas_por_categoria.index.tolist()
valores = vendas_por_categoria.values.tolist()

plt.bar(categorias, valores)

plt.title("Total de vendas por categoria")
plt.xlabel("Categorias")
plt.ylabel("Total de vendas")
plt.show()