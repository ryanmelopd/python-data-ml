import pandas as pd

dataframe = pd.read_csv("pandas-matplotlib/data/dados_funcionarios.csv")

print("\nTabela completa:")
print(dataframe)

print("\nDepartamentos existentes:")
print(dataframe["departamento"])

dataframe = dataframe.replace({
    "ti": "TI",
    "MKT": "Marketing" 
})

print("\nDepartamentos após o replace():")
print(dataframe["departamento"])