import numpy as np


def selecao_torneio(populacao, q_torneio):
    """
    Seleciona dois indivíduos com um torneio envolvendo q_torneio*len(populacao) indivíduos
    :param populacao:
    :param q_torneio: fração da quantidade de indivíduos da população selecionados por torneio
    :return: melhor indivíduo do torneio
    """
    individuos_participantes = []
    n_populacao = len(populacao)
    n_selecoes = int(q_torneio*n_populacao)
    for i in range(0, n_selecoes):
        indices_individuo_sorteado = np.random.randint(low=0, high=n_populacao)
        individuos_participantes.append(populacao[indices_individuo_sorteado, :])
    melhor_individuo = individuos_participantes[np.array(individuos_participantes)[:, 1].argmin()]
    print(melhor_individuo)
    return melhor_individuo
