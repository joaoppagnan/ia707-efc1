import numpy as np
from algoritmo_genetico import algoritmo_genetico


N_POPULACAO = 1000
CRITERIO_DE_PARADA = 10
Q_TORNEIO = 10
P_MUTACAO = 0.5
PATH_MAT_DADOS = '../dados/elshafei_QAP.mat'
N_VEZES = 1

solucoes = []
fitnesses = []
custos = []

for _ in range(0, N_VEZES):
    solucao, fitness, custo = algoritmo_genetico(n_populacao=N_POPULACAO, q_torneio=Q_TORNEIO,
                                                 criterio_de_parada=CRITERIO_DE_PARADA,
                                                 p_mutacao=P_MUTACAO, path_mat_dados=PATH_MAT_DADOS)
    solucoes.append(solucao)
    fitnesses.append(fitness)
    custos.append(custo)

print("Soluções:", solucoes)
print("Fitness:", fitnesses)
print("Custo:", custos)

print("Valor médio do custo:", np.mean(custos))
print("Desvio-padrão do custo:", np.std(custos))
