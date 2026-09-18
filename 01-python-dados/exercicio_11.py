import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_funcionarios.csv")

dataframe["salario_anual"] = dataframe["salario"] * 12

print("\nTabela completa após a nova coluna salário anual ser adicionada:")
print(dataframe)

print("\nTabela com nome, salário e salário anual:")
print(dataframe[["nome", "salario", "salario_anual"]])