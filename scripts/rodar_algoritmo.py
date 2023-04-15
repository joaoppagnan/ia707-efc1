import numpy as np
from algoritmo_genetico import algoritmo_genetico


N_POPULACAO = 1000
CRITERIO_DE_PARADA = 10
Q_TORNEIO = 0.75
P_MUTACAO = 1.0
PATH_MAT_DADOS = '../dados/elshafei_QAP.mat'

solucoes = []
fitnesses = []
custos = []

for _ in range(0, 1):
    solucao, fitness, custo = algoritmo_genetico(n_populacao=N_POPULACAO, q_torneio=Q_TORNEIO,
                                                 criterio_de_parada=CRITERIO_DE_PARADA,
                                                 p_mutacao=P_MUTACAO, path_mat_dados=PATH_MAT_DADOS)
    solucoes.append(solucao)
    fitnesses.append(fitness)
    custos.append(custo)

print(solucoes, fitnesses, custos)
