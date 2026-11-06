import numpy as np

# Gerar dados aleatórios de vendas para 4 produtos durante 3 meses
rng = np.random.default_rng(42)
vendas = rng.integers(100, 501, size=12)
print("Dados de vendas:")
print(vendas)

# 1. RESHAPE
# Transformar o array de 12 elementos em uma matriz
# com 4 linhas (produtos) e 3 colunas (meses).
vendas_matriz = vendas.reshape(4, 3)
print("\nVendas organizadas por produto e mês:")
print(vendas_matriz)


# 2. TRANSPOSE
# Transpor a matriz, invertendo linhas e colunas.
# Agora cada linha representa um mês.
vendas_transpostas = vendas_matriz.T
print("\nVendas organizadas por mês:")
print(vendas_transpostas)


# 3. BROADCASTING
# Aplicar um fator de crescimento diferente para cada mês.
# Janeiro: crescimento de 5%
# Fevereiro: crescimento de 10%
# Março: crescimento de 15%
fatores_crescimento = np.array([1.05, 1.10, 1.15])
vendas_projetadas = vendas_matriz * fatores_crescimento
print("\nProjeção de vendas:")
print(np.round(vendas_projetadas, 2))


# 4. ANÁLISE DOS RESULTADOS
# Calcular a média de vendas de cada produto.
media_produtos = np.mean(vendas_projetadas, axis=1)
print("\nMédia projetada de cada produto:")
print(np.round(media_produtos, 2))


# Encontrar o produto com a maior média de vendas.
maior_media = np.max(media_produtos)
indice_produto = np.argmax(media_produtos)
print("\nProduto com maior média de vendas:")
print("Produto:", indice_produto + 1)
print("Média:", round(maior_media, 2))


# Calcular a média geral das vendas projetadas.
media_geral = np.mean(vendas_projetadas)
print("\nMédia geral das vendas projetadas:")
print(round(media_geral, 2))