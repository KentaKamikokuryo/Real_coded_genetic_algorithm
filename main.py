# -*- coding: utf-8 -*-

from classes.Society import Society
from classes.Evaluator import *
from classes.Generator import *
from classes.Crossover import *
from classes.Generation_serector import *
from classes.Individual_selector import *

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

def get_generation_data(individual_list):

    x = [ind.gene[0] for ind in individual_list]
    y = [ind.gene[0] for ind in individual_list]

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

    for x, y in generation_data:
        im = plt.scatter(x, y, s=3, color="blue")
        ims.append([im])

    _ = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000)
    plt.show()

def plot_evaluate_values(iterator_list, list_1, list_2):

    plt.plot(iterator_list, list_1)
    plt.plot(iterator_list, list_2)
    plt.show()



