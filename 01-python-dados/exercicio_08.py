import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_empresa.csv")

media = dataframe["salario"].mean()
print("\nMédia salarial: ", media)

dataframe["salario"] = dataframe["salario"].fillna(media)

print("\nDataFrame após o preenchimento dos valores ausentes:")
print(dataframe)

print("\nValores ausentes da tabela:")
print(dataframe.isna().sum())