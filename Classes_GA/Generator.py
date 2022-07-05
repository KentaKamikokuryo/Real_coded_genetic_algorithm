# -*- coding: utf-8 -*-

import random
import numpy as np
from Classes_GA.Individual import Individual

class Generator(object):

    def __init__(self, maximum: float, minimum: float, dimention: int):

        """

        :param maximum: 遺伝子の値の上限
        :param minimum: 遺伝子の値の下限
        :param dimention: 遺伝子長
        """

        self._maximum = maximum
        self._minimum = minimum
        self._dimension = dimention

    def generate(self) :
        """
        初期遺伝子を作成する

        :return:
        """

        value_range = self._maximum - self._minimum
        gene = [value_range * np.random.rand() + self._minimum for _ in range(self._dimension)]
        return Individual(gene)