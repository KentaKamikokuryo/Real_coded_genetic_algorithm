# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import random
from Classes_GA.Individual_selector import *

class GenerationSelector(ABC):
    """
    次世代に残す個体の選択方法のベース
    """

    @abstractmethod
    def select(self, individuals: list, parents_list: list, children: list):
        """
        次世代に残す個体のリストを返す
        :param individuals: 個体のリスト
        :param parents_list: 親個体のIndexのリスト
        :param children: 生成した子個体
        :return:
        """
        pass

class MGG(GenerationSelector):
    """
    Minimum Generation Gap による世代交代
    """
    def select(self, individuals, parents_list, children):
        """
        次世代に残す個体のリスト(集団)を返す
        親個体＋子個体からエリート1個体，ルーレット1個体を選択肢し，親個体と入れ替える

        :param individuals:
        :param parents_list:
        :param children:
        :return:
        """

        # 親となった個体を取得
        target = [individuals[x] for x in parents_list]

        # 次世代に加える候補を作成
        target.extend(children)

        remain = []
        # エリート選択とルーレット選択で次世代を追加
        elite = EliteSelector(1).select(target)
        remain.extend([target.pop(x) for x in elite])
        roulette = RouletteSelector(1).select(target)
        remain.extend([target.pop(x) for x in roulette])

        # 個体入れ替え
        for p, r in zip(parents_list, remain):
            individuals[p] = children[r]

        return individuals

class JGG(GenerationSelector):

    """
    Just Generation Gap による世代交代
    """

    def select(self, individuals: list, parents_list: list, children: list):
        """
        次世代に残す個体のリストを返す
        子個体からエリート個体を選択し，親個体と入れ替える

        :param individuals:
        :param parents_list:
        :param children:
        :return:
        """

        elite = EliteSelector(len(parents_list)).select(children)

        for p, e in zip(parents_list, elite):

            individuals[p] = children[e]

        return individuals