import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_vendas.csv")

dataframe["total_vendas"] = dataframe["preco"] * dataframe["quantidade"]

quantidade_por_vendedor = dataframe.groupby("vendedor")["quantidade"].sum()
vendedor = quantidade_por_vendedor.idxmax()
print("\nVendedor que teve mais unidades vendidas: ", vendedor)

print("\nTotal de vendas de cada vendedor:")
print(dataframe.groupby("vendedor")["total_vendas"].sum())

print("\nTotal de vendas que foram superiores a R$5.000:")
print(dataframe[dataframe["total_vendas"] > 5000])

print("\nProdutos que foram vendidos em quantidade igual ou superior a 5 unidades:")
print(dataframe[dataframe["quantidade"] >= 5][["produto", "quantidade"]])

print("\nTotal de vendas por categoria:")
print(dataframe.groupby("categoria")["total_vendas"].sum())

print("\nTabela contendo produto, vendedor, quantidade e total de vendas:")
print(dataframe.sort_values(by="total_vendas", ascending=False)[["produto", "vendedor", "quantidade", "total_vendas"]])