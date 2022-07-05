# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import numpy as np
import random

class IndividualSelector(ABC):
    """
    個体の選択方法
    """

    def __init__(self, selection_num):
        self._selection_num = selection_num

    @abstractmethod
    def select(self, individuals: list):
        """
        選択した個体のリストを返す
        :param individuals: 個体のリスト
        :return:
        """

        pass

class EliteSelector(IndividualSelector):

    def select(self, individuals: list):
        """
        評価値の低いものから選択する
        :param individuals: 個体リスト
        :return:
        """

        evaluate_list = np.array([x.evaluate_value for x in individuals])

        return np.argsort(evaluate_list)[:self._selection_num]

class RouletteSelector(IndividualSelector):

    def select(self, individuals: list):
        """
        評価値が小さいものを選択肢しやすくし，ルーレットで選ぶ
        :param individuals:
        :return:
        """

        evaluate_list = np.array([x.evaluate_value for x in individuals])

        evaluate_list = np.abs(evaluate_list - np.max(evaluate_list))
        total = np.sum(evaluate_list)

        selected_index = []
        for _ in range(self._selection_num):

            threshold = random.uniform(0.0, total)

            sum = 0.0
            for index, value in enumerate(evaluate_list):

                sum += value

                if sum >= threshold:

                    # 選択されたIndexは次の選択から除く
                    selected_index.append(index)
                    evaluate_list[index] = 0.
                    total -= value

                    break

        return selected_index