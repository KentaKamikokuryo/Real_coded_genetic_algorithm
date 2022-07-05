# -*- coding: utf-8 -*-
import numpy as np

class Society(object):

    def __init__(self,
                 evaluator,
                 crossover,
                 parent_selector,
                 generation_selector):

        """
        Constractor

        :param evaluator: 評価関数
        :param crossover: 交叉
        :param parent_selector: 親を選択するセレクタ
        :param generation_selector: 次世代を選択するセレクタ
        """

        self._evaluator = evaluator
        self._crossover = crossover
        self._parent_selector = parent_selector
        self._generation_selector = generation_selector
        self._individuals = None

    def generate_individuals(self, size: int, generator):
        """
        初期個体を生成する

        :param size: 生成する個体数
        :param generator: 生成関数
        :return:
        """

        self._individuals = [generator.generate() for _ in range(size)]

    def get_best_individual(self):
        """
        評価値の最良の個体を返す

        :return:
        """

        temp_evaluate = np.array([x.evaluate_value for x in self._individuals])

        return self._individuals[np.argmin(temp_evaluate)]

    def change_generation(self):
        """
        世代交代を担う
        :return:
        """

        # 親個体のインデックスを選択
        parents_index = self._parent_selector.select(self._individuals)

        # 交叉
        children = self._crossover.crossover(self._individuals, parents_index)

        # 全個体から次の世代を選択する
        self._individuals = self._generation_selector.select(self._individuals, parents_index, children)


    @property
    def individuals(self):
        return self._individuals
