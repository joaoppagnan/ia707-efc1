import numpy as np
import scipy.io
from calc_custo_qap import calc_custo_qap


def calc_fitness_qap(populacao, distancias, fluxos):
    """
    Calcula o fitness para um problema do tipo QAP
    :param populacao: populacao que terá o fitness calculado
    :param distancias: distância entre as localidades
    :param fluxos: fluxo entre as instalações
    :return: a população com o fitness atualizado
    """
    n_alelos = fluxos.shape[0]
    for individuo in populacao:
        if individuo[1] == 0:
            fitness = (1/calc_custo_qap(individuo=individuo, distancias=distancias, fluxos=fluxos))/(1/17212548)
            individuo[1] = fitness
    return populacao
