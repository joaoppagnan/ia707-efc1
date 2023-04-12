import numpy as np
import scipy.io


def calc_fitness_QAP(populacao, n_alelos, distancias, fluxos):
    """
    Calcula o fitness para um problema do tipo QAP
    :param populacao: populacao que terá o fitness calculado
    :param n_alelos: quantidade de alelos no código genético da população
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: um array com os fitness
    """
    fitness_pop = []
    for k in range(0, len(populacao)):
        try:
            individuo = populacao[k, 0]
        except:
            individuo = populacao[k]
        fitness = 0
        casos_vistos = []
        for i in range(0, n_alelos):
            for j in range(0, n_alelos):

                # para evitar casos repetidos
                if (i, j) in casos_vistos or (j, i) in casos_vistos: continue

                fitness += distancias[i, j]*fluxos[individuo[i], individuo[j]]
                casos_vistos.append((i, j))
        fitness_pop.append(fitness)
    return np.array(fitness_pop)