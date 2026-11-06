import numpy as np

# Matriz com o desempenho de 5 funcionários durante 3 meses
desempenho = np.array([
    [80, 85, 90],
    [70, 75, 80],
    [90, 95, 100],
    [60, 70, 75],
    [85, 80, 90]
])

print("Desempenho dos funcionários:")
print(desempenho)

print("Quantidade de dimensões da matriz: ", desempenho.ndim)

print("Formato da matriz: ", desempenho.shape)

print("Quantidade total de elementos: ", desempenho.size)

media_geral = np.mean(desempenho)
print("Média geral: ", media_geral)


media_funcionarios = np.mean(desempenho, axis=1)
print("Média de cada funcionário:")
print(np.round(media_funcionarios, 2))


media_meses = np.mean(desempenho, axis=0)
print("Média de cada mês:")
print(np.round(media_meses, 2))


maior_media = np.max(media_funcionarios)
indice_funcionario = np.argmax(media_funcionarios)
print("Funcionário com maior média:")
print("Funcionário: ", indice_funcionario + 1)
print("Média: ", maior_media)


maior_media_mes = np.max(media_meses)
indice_mes = np.argmax(media_meses)
print("Mês com maior média:")
print("Mês:", indice_mes + 1)
print("Média:", maior_media_mes)


novo_desempenho = desempenho + 5
print("Desempenho atualizado após adicionar 5 pontos a todos os valores:")
print(novo_desempenho)


funcionarios_destaque = np.where(media_funcionarios >= 85)[0] + 1
print("Funcionários com média > 85:")
print(funcionarios_destaque)