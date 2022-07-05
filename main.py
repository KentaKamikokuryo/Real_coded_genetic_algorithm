# -*- coding: utf-8 -*-
import os
from Classes_GA.Society import Society
from Classes_GA.Evaluator import *
from Classes_GA.Generator import *
from Classes_GA.Crossover import *
from Classes_GA.Generation_serector import *
from Classes_GA.Individual_selector import *
from Classes.Info import PathInfo

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

def plot_transition(x, y, generation_data):

    fig, (axL, _) = plt.subplots(ncols=2, figsize=(10, 4))

    # 左のプロット
    axL.plot(x, y, linewidth=2)
    axL.set_title("iterate - best value")
    axL.set_xlabel("iterate")
    axL.set_ylabel("evaluate value")
    axL.grid(True)

    # 右のプロット
    ims = []

    print("In the process of creating an animation...")

    for x, y in generation_data:

        im = plt.scatter(x, y, s=3, color="blue")
        ims.append([im])

    print("Animation creation is complete")
    _ = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
    plt.show()

def animate_transition_new(x, y, generation_data, path):

    ncols = 1
    nrows = 2

    fig = plt.figure(figsize=(10, 4))
    gs = gridspec.GridSpec(ncols, nrows, width_ratios=(1, 1))
    ax = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1:])

    filenames = []
    gif_name = "gif_transion"

    for i in range(len(x)):

        filename = "temp_" + str(i) + "_" + str(1)
        filenames.append(filename)
        fig.suptitle("GENERATION: " + str(i))

        ax.plot(x[:i], y[:i], linewidth=2)
        ax.set_xlabel("iteration")
        ax.set_ylabel("evaluate value")
        ax.set_xlim(0, len(x))
        ax.set_ylim(0, np.max(y) + 10)
        ax.grid(True)

        ax2.scatter(generation_data[i][0], generation_data[i][1], s=3, color="blue")
        ax2.set_xlim(np.min(generation_data[:][0]), np.max(generation_data[:][0]))
        ax2.set_ylim(np.min(generation_data[:][1]), np.max(generation_data[:][1]))

        plt.savefig(path + filename, dpi=150)

        ax.cla()
        ax2.cla()

    print("Creating .gif (Take time)")

    with imageio.get_writer(path + gif_name + ".gif", mode="I") as writer:
        for filename in filenames:
            image = imageio.imread(path + filename + ".png")
            writer.append_data(image)

    print("Saving Gaussian .gif to: " + str(path + gif_name + ".gif"))

    for filename in set(filenames):
        os.remove(path + filename + ".png")




def plot_evaluate_values(iterator_list, list_1, list_2):

    plt.plot(iterator_list, list_1)
    plt.plot(iterator_list, list_2)
    plt.show()

def demo_1():

    # 遺伝子長
    dimension = 50

    # 集団数
    individual_num = 300

    # 選択数
    selection_num = 500

    # 世代数の最大
    generation_loop = 1000

    # 評価関数
    evaluator = Rastrigin()

    # 次世代に残す個体の選択
    society = Society(evaluator=evaluator,
                      crossover=Simplex(selection_num),
                      parent_selector=RouletteSelector(dimension),
                      generation_selector=JGG())

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
    # plot_transition(iterate, best_value, generation_data)
    pathInfo = PathInfo()
    animate_transition_new(iterate, best_value, generation_data, pathInfo.folder_GA)

demo_1()

