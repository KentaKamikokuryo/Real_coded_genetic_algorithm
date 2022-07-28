# -*- coding: utf-8 -*-
import os
from Classes_GA.Society import Society
from Classes_GA.Evaluator import *
from Classes_GA.Generator import *
from Classes_GA.Generation_serector import *
from Classes_GA.Crossover import *
from Classes.Info import PathInfo
from Classes.Plot import Plot
from Classes.Factories import *
from Classes_GA.Individual_selector import *
from Classes.Models import Models


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import gridspec
import imageio
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def get_generation_data(individual_list):

    x = [ind.gene[0] for ind in individual_list]
    y = [ind.gene[1] for ind in individual_list]

    return (x, y)

def demo(arguments: dict):

    model_name = arguments["model_name"]

    # 遺伝子長
    dimension = 50

    # 集団数
    individual_num = arguments["individual_name"]

    # 選択数 (交叉が生成する子個体の数)
    selection_num = dimension * 10

    # 世代数の最大
    generation_loop = 1000

    # 評価関数
    evaluator = Rastrigin()

    cofac = CrossoverFactory(model_name=arguments["co_name"], selection_num=selection_num)
    gsfac = GenerationSelectorFactory(model_name=arguments["gs_name"])

    # 次世代に残す個体の選択
    society = Society(evaluator=evaluator,
                      crossover=cofac.create(),
                      parent_selector=EliteSelector(dimension + 1),
                      generation_selector=gsfac.create())

    # 初期個体の生成
    generator = Generator(maximum=5.12, minimum=-5.12, dimention=dimension)
    society.generate_individuals(size=individual_num, generator=generator)

    # 画像データ表示用
    best_value = []
    iterate = []
    generation_data = []
    generation_data.append(get_generation_data(society.individuals))

    # 遺伝的操作を行う
    for i in range(generation_loop):

        society.change_generation()

        # 画像データ表示用処理
        best = society.get_best_individual()
        iterate.append(i)
        best_value.append(best.evaluate_value)
        generation_data.append(get_generation_data(society.individuals))

        best = society.get_best_individual()
        print("GENERATION: " + str(i) + " - " + "EVALUATE VALUE: " + str(best.evaluate_value))

    # 最良評価値の推移を表示
    plot = Plot()
    pathInfo = PathInfo()
    np.save(pathInfo.folder_hist + model_name + ".npy", np.array(best_value))
    plot.animate_transition_new(iterate, best_value, generation_data, pathInfo.folder_GA, model_name)

models = Models()

# demo(models._model_bench)
# demo(models.model_1)
# demo(models._model_2)
# demo(models._model_3)
# demo(models._model_4)
# demo(models._model_5)
demo(models.test)

