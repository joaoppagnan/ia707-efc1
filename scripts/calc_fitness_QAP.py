import numpy as np
import scipy.io


def calc_fitness_QAP(populacao, distancias, fluxos):
    """
    Calcula o fitness para um problema do tipo QAP
    :param populacao: populacao que terá o fitness calculado
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: a população com o fitness atualizado
    """
    n_alelos = fluxos.shape[0]
    fitness_pop = []
    for individuo in populacao:
        fitness = 0
        casos_vistos = []
        for i in range(0, n_alelos):
            for j in range(0, n_alelos):

                # para evitar casos repetidos
                if (i, j) in casos_vistos or (j, i) in casos_vistos:
                    continue

                fitness += distancias[i, j]*fluxos[individuo[0][i], individuo[0][j]]
                casos_vistos.append((i, j))
        individuo[1] = fitness
    return populacao
