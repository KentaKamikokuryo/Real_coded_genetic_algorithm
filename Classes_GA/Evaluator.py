# -*- coding: utf-8 -*-

import math
from abc import ABC, abstractmethod
from Classes_GA.Individual import Individual

class Evaluator(ABC):

    def __init__(self):

        Individual.set_evaluator(evaluator=self)

    def evaluate(self, individual):

        return self._evaluate_function(individual.gene)

    @abstractmethod
    def _evaluate_function(self, gene):

        pass


class Rastrigin(Evaluator):

    def _evaluate_function(self, gene):

        value=0

        for x in gene:
            value += 10 + (x*x - 10 * math.cos(2*math.pi*x))

        return value


