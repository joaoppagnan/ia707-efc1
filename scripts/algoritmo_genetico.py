import numpy as np
import scipy.io
from gerar_pop import gerar_pop
from calc_fitness_QAP import calc_fitness_QAP
from selecao_torneio import selecao_torneio


class AlgoritmoGeneticoQAP(object):
    def __init__(self, N_populacao: int, n_geracoes: int, q_torneio: float, criterio_de_parada: float,
                 path_mat_dados: str = 'dados/elshafei_QAP.mat'):
        """
        Construtor do algoritmo genetico
        :param int N_populacao: número de indivíduos na população
        :param int n_geracoes: quantidade de geracoes
        :param float q_torneio: fração da população presente no torneio
        :param float criterio_de_parada: critério de parada a ser utilizado
        :param str path_mat_dados: arquivo que os dados estão armazenados
        """
        mat_dados = scipy.io.loadmat(path_mat_dados)
        self.distancias = mat_dados['D']
        self.fluxos = mat_dados['W']
        self.N_populacao = N_populacao
        self.n_geracoes = n_geracoes
        self.q_torneio = q_torneio
        self.criterio_de_parada = criterio_de_parada

    def algoritmo_genetico(N_populacao, n_geracoes, q_torneio, criterio_de_parada):
        """
        Funcao principal do algoritmo genetico
        :param N_populacao: número de indivíduos na população
        :param n_geracoes: quantidade de geracoes
        :param q_torneio: fração da população presente no torneio
        :param criterio_de_parada: critério de parada a ser utilizado
        :return: melhor individuo e melhor fitness
        """

        # gerar população inicial
        populacao_ini = gerar_pop(N_populacao, )