import numpy as np
import pandas as pd

# Carregar o dataset iris.csv.
# O arquivo deve estar na mesma pasta deste código.
flores = pd.read_csv("numpy/data/iris.csv")

print("Primeiras linhas do dataset:")
print(flores.head())


# 1. EXPLORAÇÃO INICIAL COM PANDAS
# Consultar dimensões, informações e estatísticas do dataset.
print("\nDimensões do dataset:")
print("Linhas e colunas:", flores.shape)

print("\nInformações das colunas:")
flores.info()

print("\nEstatísticas descritivas:")
print(flores.describe())

# Contar a quantidade de flores por espécie.
print("\nQuantidade de flores por espécie:")
print(flores["especie"].value_counts())


# 2. CONVERSÃO PARA NUMPY
# Selecionar somente as quatro características numéricas.
caracteristicas = flores[
    [
        "comprimento_sepala_cm",
        "largura_sepala_cm",
        "comprimento_petala_cm",
        "largura_petala_cm"
    ]
]

# Converter o DataFrame em um array NumPy.
dados_numpy = caracteristicas.to_numpy()

print("\nArray NumPy:")
print(dados_numpy)

# Consultar as propriedades do array.
print("\nPropriedades do array:")
print("Dimensões:", dados_numpy.ndim)
print("Formato:", dados_numpy.shape)
print("Quantidade de elementos:", dados_numpy.size)


# 3. CÁLCULOS ESTATÍSTICOS COM NUMPY
# Calcular a média de cada característica.
medias = np.mean(dados_numpy, axis=0)

print("\nMédia de cada característica:")
print(np.round(medias, 2))

# Encontrar os maiores e menores valores de cada característica.
maiores_valores = np.max(dados_numpy, axis=0)
menores_valores = np.min(dados_numpy, axis=0)

print("\nMaiores valores:")
print(maiores_valores)

print("\nMenores valores:")
print(menores_valores)


# 4. ANÁLISE POR ESPÉCIE COM PANDAS + NUMPY
# Separar as flores da espécie setosa e converter para NumPy.
flores_setosa = flores[flores["especie"] == "setosa"]

setosa_numpy = flores_setosa[
    [
        "comprimento_sepala_cm",
        "largura_sepala_cm",
        "comprimento_petala_cm",
        "largura_petala_cm"
    ]
].to_numpy()

# Calcular a média das características da espécie setosa.
media_setosa = np.mean(setosa_numpy, axis=0)

print("\nMédias da espécie setosa:")
print(np.round(media_setosa, 2))


# Repetir a análise para a espécie versicolor.
flores_versicolor = flores[flores["especie"] == "versicolor"]

versicolor_numpy = flores_versicolor[
    [
        "comprimento_sepala_cm",
        "largura_sepala_cm",
        "comprimento_petala_cm",
        "largura_petala_cm"
    ]
].to_numpy()

media_versicolor = np.mean(versicolor_numpy, axis=0)

print("\nMédias da espécie versicolor:")
print(np.round(media_versicolor, 2))


# Repetir a análise para a espécie virginica.
flores_virginica = flores[flores["especie"] == "virginica"]

virginica_numpy = flores_virginica[
    [
        "comprimento_sepala_cm",
        "largura_sepala_cm",
        "comprimento_petala_cm",
        "largura_petala_cm"
    ]
].to_numpy()

media_virginica = np.mean(virginica_numpy, axis=0)

print("\nMédias da espécie virginica:")
print(np.round(media_virginica, 2))


# 5. BROADCASTING
# Aplicar um aumento ilustrativo de 10% em todas as medidas.
dados_aumentados = dados_numpy * 1.10

print("\nPrimeiras 5 linhas com aumento de 10%:")
print(np.round(dados_aumentados[:5], 2))


# 6. FILTROS COM PANDAS
# Encontrar flores com comprimento de pétala maior que 5 cm.
petalas_grandes = flores[flores["comprimento_petala_cm"] > 5]

print("\nFlores com pétalas maiores que 5 cm:")
print(petalas_grandes.head())
print("Quantidade encontrada:", len(petalas_grandes))


# 7. COMPARAÇÃO FINAL
# Calcular a média do comprimento da pétala por espécie.
medias_petala = flores.groupby("especie")["comprimento_petala_cm"].mean()

print("\nMédia do comprimento da pétala por espécie:")
print(medias_petala.round(2))

# Encontrar a espécie com a maior média.
especie_maior_media = medias_petala.idxmax()
maior_media_petala = medias_petala.max()

print("\nEspécie com maior média de comprimento da pétala:")
print("Espécie:", especie_maior_media)
print("Média:", round(maior_media_petala, 2))