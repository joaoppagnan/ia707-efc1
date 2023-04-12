import numpy as np


def gerar_pop(N, n):
    """
    Gera a população inicial com base em uma permutação aleatória
    :param N: tamanho da população inicial
    :param n: quantidade de alelos
    :return: população inicial num array do numpy
    """
    populacao = []
    for i in range(0, N):
        individuo = []
        for j in range(0, n):
            gene = np.random.randint(low=0, high=n)
            while gene in individuo:
                gene = np.random.randint(low=0, high=n)
            individuo.append(gene)
        populacao.append(individuo)
    return np.array(populacao)
