import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 10.0, 8.5, 7.0])

print("Todas as notas dos alunos: ", notas)

print("Quantidade de alunos: ", notas.size)

print("Média das notas: ", np.mean(notas))

print("Maior nota:", np.max(notas))
print("Menor nota:", np.min(notas))

print("Mediana das notas: ", np.median(notas))

print("Desvio padrão das notas: ", np.std(notas))

aprovados = notas[notas >= 7]
print("Array de alunos aprovados: ", aprovados)

print("Quantidade de alunos aprovados:", aprovados.size)

novas_notas = np.minimum(notas + 0.5, 10)
print("Notas atualizadas adicionando 0,5 pontos, limitando a nota máxima em 10:")
print(novas_notas)