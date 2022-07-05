# -*- coding: utf-8 -*-

from Classes_GA.Evaluator import *
import numpy as np

class Individual():

    _evaluator = None

    def __init__(self, gene):

        self._gene = np.array(gene)
        self._evaluate_value = Individual._evaluator.evaluate(self)

    @classmethod
    def set_evaluator(cls, evaluator):

        Individual._evaluator = evaluator

    @property
    def gene(self):

        return self._gene

    @property
    def evaluate_value(self):

        return self._evaluate_value