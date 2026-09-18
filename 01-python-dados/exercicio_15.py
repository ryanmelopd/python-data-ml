import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_vendas.csv")

dataframe["total_vendas"] = dataframe["preco"] * dataframe["quantidade"]

print("\nTotal de vendas de cada vendedor:")
print(dataframe.groupby("vendedor")["total_vendas"].sum())

print("\nQuantidade total de produtos vendidos por vendedor:")
print(dataframe.groupby("vendedor")["quantidade"].sum())

print("\nPreço médio dos produtos vendidos por cada vendedor:")
print(dataframe.groupby("vendedor")["preco"].mean())

valor_total_por_vendedor = dataframe.groupby("vendedor")["total_vendas"].sum()
vendedor = valor_total_por_vendedor.idxmax()
print("\nVendedor que teve maior valor total de vendas: ", vendedor)

dataframe["ticket_medio"] = dataframe["total_vendas"] / dataframe["quantidade"]

print("\nTabela contendo vendedor, total de vendas, quantidade e a nova coluna adicionada ticket médio:")
print(dataframe.sort_values(by="total_vendas", ascending=False)[["vendedor", "total_vendas", "quantidade", "ticket_medio"]])