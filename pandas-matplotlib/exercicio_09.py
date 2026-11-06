import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_empresa.csv")

print("\nTabela:")
print(dataframe)

print("\nValores ausentes existentes:")
print(dataframe.isna().sum())

dataframe = dataframe.dropna()
print("\nTabela após a remoção dos valores ausentes:")
print(dataframe)

print("\nValores ausentes após o uso de dropna():")
print(dataframe.isna().sum())