import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_vendas.csv")

print("\nTabela completa:")
print(dataframe)

media = dataframe["preco"].mean()
print("\nPreço médio dos produtos: ", media)

indice = dataframe["preco"].idxmax()
print("\nProduto mais caro:")
print(dataframe.loc[indice, ["produto", "preco"]])

indice = dataframe["preco"].idxmin()
print("\nProduto mais barato:")
print(dataframe.loc[indice, ["produto", "preco"]])

print("\nQuantos produtos existem em cada categoria:")
print(dataframe.groupby("categoria")["produto"].count())

print("\nPreço médio por categoria:")
print(dataframe.groupby("categoria")["preco"].mean())

print("\nProdutos que possuem preço acima da média geral:")
print(dataframe[dataframe["preco"] > media][["produto", "preco"]])

print("\nProdutos ordenados do mais caro para o mais barato:")
print(dataframe.sort_values(by="preco", ascending=False))

print("\nProdutos com a tabela mostrando apenas produto, preço e quantidade:")
print(dataframe[["produto", "preco", "quantidade"]])

dataframe["total_vendas"] = dataframe["preco"] * dataframe["quantidade"]
print("\nTabela com nova coluna adicionada:")
print(dataframe)

print("\nProdutos ordenados pelo total de vendas, do maior para o menor:")
print(dataframe.sort_values(by="total_vendas", ascending=False))




