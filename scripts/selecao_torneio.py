import numpy as np


def selecao_torneio(populacao, q_torneio):
    """
    Seleciona dois indivíduos com um torneio envolvendo q_torneio*len(populacao) indivíduos
    :param populacao:
    :param q_torneio: fração da quantidade de indivíduos da população selecionados por torneio
    :return: melhor indivíduo do torneio
    """
    individuos_participantes = []
    N_populacao = len(populacao)
    n_selecoes = q_torneio*N_populacao
    for i in range(0, n_selecoes):
        individuo_sorteado = np.random.randint(low=0, high=N_populacao)
        individuos_participantes.append(populacao[individuo_sorteado,:])
    indice_melhor_individuo = np.argsort(individuos_participantes[:, 1])
    melhor_individuo = populacao[indice_melhor_individuo, :]
    return melhor_individuo