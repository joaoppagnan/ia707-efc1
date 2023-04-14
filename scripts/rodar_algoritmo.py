import numpy as np
from algoritmo_genetico import algoritmo_genetico


N_POPULACAO = 100
CRITERIO_DE_PARADA = 1e-2
Q_TORNEIO = 0.75
P_MUTACAO = 0.3
PATH_MAT_DADOS = '../dados/elshafei_QAP.mat'


algoritmo_genetico(n_populacao=N_POPULACAO, q_torneio=Q_TORNEIO, criterio_de_parada=CRITERIO_DE_PARADA,
                   p_mutacao=P_MUTACAO, path_mat_dados=PATH_MAT_DADOS)
