from Classes_GA.Crossover import CrossoverName
from Classes_GA.Generation_serector import GenerationSelectorName
from Classes_GA.Crossover import CrossoverName

class Models():

    def __init__(self):

        self._model_bench = {"co_name": CrossoverName.BLX_a,
                             "gs_name": GenerationSelectorName.MGG,
                             "individual_name": 300,
                             "model_name": "Benchmark"}

        self._model_1 = {"co_name": CrossoverName.SPX,
                         "gs_name": GenerationSelectorName.MGG,
                         "individual_name": 300,
                         "model_name": "model_1"}

        self._model_2 = {"co_name": CrossoverName.BLX_a,
                         "gs_name": GenerationSelectorName.JGG,
                         "individual_name": 300,
                         "model_name": "model_2"}

        self._model_3 = {"co_name": CrossoverName.BLX_a,
                         "gs_name": GenerationSelectorName.MGG,
                         "individual_name": 100,
                         "model_name": "model_3"}

        self._model_4 = {"co_name": CrossoverName.BLX_a,
                         "gs_name": GenerationSelectorName.MGG,
                         "individual_name": 500,
                         "model_name": "model_4"}

        self._model_5 = {"co_name": CrossoverName.SPX,
                         "gs_name": GenerationSelectorName.JGG,
                         "individual_name": 500,
                         "model_name": "model_5"}

        self._test = {"co_name": CrossoverName.SPX,
                      "gs_name": GenerationSelectorName.JGG,
                      "individual_name": 500,
                      "model_name": "test"}

    @property
    def model_1(self):
        return self._model_1

    @property
    def model_2(self):
        return self._model_2

    @property
    def model_3(self):
        return self._model_3

    @property
    def model_4(self):
        return self._model_4

    @property
    def model_5(self):
        return self._model_5

    @property
    def test(self):
        return self._test
