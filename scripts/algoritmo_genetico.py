import numpy as np
import scipy.io
from gerar_pop import gerar_pop
from calc_fitness_QAP import calc_fitness_QAP
from selecao_torneio import selecao_torneio


def algoritmo_genetico(n_populacao: int, q_torneio: float, criterio_de_parada: float,
                       path_mat_dados: str):
    """
    Funcao principal do algoritmo genetico
    :param n_populacao: número de indivíduos na população
    :param q_torneio: fração da população presente no torneio
    :param criterio_de_parada: critério de parada a ser utilizado
    :param str path_mat_dados: caminho para a matriz com os dados
    :return: melhor individuo e melhor fitness
    """

    # carrega os dados
    mat_dados = scipy.io.loadmat(path_mat_dados)
    distancias = mat_dados['D']
    fluxos = mat_dados['W']

    # vê quantos alelos serão necessários
    n_alelos = fluxos.shape[0]

    # gerar população inicial
    pop_ini = gerar_pop(n_populacao, n_alelos)

    # calcula o fitness para ela
    pop_ini = calc_fitness_QAP(pop_ini, distancias, fluxos)