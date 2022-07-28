# -*- coding: utf-8 -*-
from Classes_GA.Crossover import *
from Classes_GA.Generation_serector import *
from abc import ABC, abstractmethod, abstractproperty

class IFactory(ABC):

    @abstractmethod
    def create(self):
        pass

class CrossoverFactory(IFactory):

    def __init__(self, model_name: str, selection_num: int):

        self.model_name = model_name
        self.selection_num = selection_num

    def create(self) -> Crossover:

        if self.model_name == CrossoverName.BLX_a:

            model = BLX_alpha(generate_size=self.selection_num)

        elif self.model_name == CrossoverName.SPX:

            model = Simplex(generate_size=self.selection_num)

        else:

            model = BLX_alpha(generate_size=self.selection_num)

        return model

class GenerationSelectorFactory(IFactory):

    def __init__(self, model_name: str):

        self.model_name = model_name

    def create(self) -> GenerationSelector:

        if self.model_name == GenerationSelectorName.MGG:

            model = MGG()

        elif self.model_name == GenerationSelectorName.JGG:

            model = JGG()

        else:

            model = MGG()

        return model


