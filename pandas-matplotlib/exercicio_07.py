import pandas as pd

dataframe = pd.read_csv("pandas-matplotlib/data/dados_empresa.csv")

print("\nTabela completa:")
print(dataframe)

print("\nValores ausentes em cada coluna:")
print(dataframe.isna().sum())

print("\nSalário médio:")
print(dataframe["salario"].mean())

print("\nMédia salarial por departamento:")
print(dataframe.groupby("departamento")["salario"].mean())

