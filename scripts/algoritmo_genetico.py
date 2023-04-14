import numpy as np
import scipy.io
from gerar_pop import gerar_pop
from calc_fitness_qap import calc_fitness_qap
from selecao_torneio import selecao_torneio
from recombinacao_ox import recombinacao_ox
from mutacao_reversao import mutacao_reversao
from calc_custo_qap import calc_custo_qap


def algoritmo_genetico(n_populacao: int, q_torneio: float, criterio_de_parada: float, p_mutacao:float,
                       path_mat_dados: str):
    """
    Funcao principal do algoritmo genetico
    :param n_populacao: número de indivíduos na população
    :param q_torneio: fração da população presente no torneio
    :param criterio_de_parada: critério de parada a ser utilizado
    :param p_mutacao: probabilidade de acontecer uma mutação
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
    populacao = gerar_pop(n_populacao, n_alelos)

    # calcula o fitness para ela
    populacao = calc_fitness_qap(populacao, distancias, fluxos)

    # inicializa a variável do melhor fitness para checar com o critério de parada
    fitness_medio = np.average(populacao[:, 1])
    delta_fitness = fitness_medio

    # entra no loop principal do algoritmo
    while delta_fitness >= criterio_de_parada:
        fitness_anterior = fitness_medio

        # agora vai realizar a seleção -> recombinação -> mutação até que a população aumente para 3N/2 individuos
        while len(populacao) < 2*n_populacao:

            # seleciona dois pais
            pais = []
            for i in range(0, 2):
                pai = selecao_torneio(populacao=populacao, q_torneio=q_torneio)
                pais.append(pai)

            # realiza a recombinação para produzir um descendente
            descendentes = recombinacao_ox(cromossomo_p1=pais[0][0], cromossomo_p2=pais[1][0])

            # realiza a mutação com uma chance dada por pm
            for descendente in descendentes:
                descendente[0] = mutacao_reversao(cromossomo=descendente[0], p_mutacao=p_mutacao)
