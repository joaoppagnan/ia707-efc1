import numpy as np
import scipy.io


def calc_fitness_QAP(individuo, n_alelos, distancias, fluxos):
    """
    Calcula o fitness para um problema do tipo QAP
    :param individuo: individuo que terá o fitness calculado
    :param n_alelos: quantidade de alelos no código genético da população
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: um array com os fitness
    """
    fitness = 0
    casos_vistos = []
    for i in range(0, n_alelos):
        for j in range(0, n_alelos):

            # para evitar casos repetidos
            if (i, j) in casos_vistos or (j, i) in casos_vistos: continue

            fitness += distancias[i, j]*fluxos

