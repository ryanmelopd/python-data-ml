import pandas as pd

dataframe = pd.read_csv("01-python-dados/data/dados_funcionarios.csv")

def classificar_salario(salario):
    if (salario > 7000):
        return "Alto"
    elif (salario >= 4000 and salario <= 7000):
        return "Médio"
    else:
        return "Baixo"

dataframe["classificacao"] = dataframe["salario"].apply(classificar_salario)

print("\nTabela completa após adicionar uma nova coluna chamada classificação:")
print(dataframe)

