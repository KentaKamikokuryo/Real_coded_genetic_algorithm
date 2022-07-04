# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import random
import math
import numpy as np
from classes.Individual import Individual
from typing import List

class Crossover(ABC):

    def __init__(self, generate_size: int):
        """
        Constractor

        :param generate_size: 交叉によって生成する個体数
        """

        self._generate_size = generate_size

    @abstractmethod
    def crossover(self, individuals: List[Individual], parent_list: list) -> list:
        """

        :param individual: 個体群
        :param parent_list: 個体群の中から使用する親
        :return: 生成した子個体
        """

        pass

class BLX_alpha(Crossover):

    def __init__(self, generate_size, alpha=0.3):
        super(BLX_alpha, self).__init__(generate_size)
        self._alpha = alpha

    def crossover(self, individuals: List[Individual], parent_list: list) -> list:

        matrix = np.array([individuals[x].gene for x in parent_list[:2]])
        gene_max = matrix.max(axis=0)
        gene_min = matrix.min(axis=0)
        gene_abs = np.abs(gene_max - gene_min)

        gene_max = gene_max + self._alpha * gene_abs
        gene_min = gene_min + self._alpha * gene_abs

        result = []

        for _ in range(self._generate_size):

            gene = [random.uniform(g_min, g_max) for g_max, g_min in zip(gene_max, gene_min)]
            result.append(gene)

        return result

class Simplex(Crossover):

    def crossover(self, individuals: List[Individual], parent_list: list) -> list:

        matrix = np.array([individuals[x].gene for x in parent_list])
        center = matrix.mean(axis=0)

        dimension = len(center)
        epsilon = math.sqrt(dimension + 2)

        matrix = center + epsilon * (matrix - center)

        result = []
        for _ in range(self._generate_size):

            gene = np.zeros(dimension)

            for k, (vector1, vector2) in enumerate(zip(matrix, matrix[1:])):

                r_k = random.uniform(0., 1.) ** (1./(k+1))
                gene = r_k * (vector1 - vector2 + gene)

            gene += matrix[-1]
            result.append(Individual(gene))

        return result

