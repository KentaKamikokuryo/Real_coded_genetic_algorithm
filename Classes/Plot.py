import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import gridspec
import imageio
import numpy as np
import os
import seaborn as sns

class Plot():

    def __init__(self):

        sns.set(style='ticks', rc={"grid.linewidth": 0.1})
        sns.set_context("paper", font_scale=1.5)
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'

    @staticmethod
    def plot_transition(x, y):
        fig, (axL, _) = plt.subplots(ncols=2, figsize=(10, 4))

        # 左のプロット
        axL.plot(x, y, linewidth=2)
        axL.set_title("iterate - best value")
        axL.set_xlabel("iterate")
        axL.set_ylabel("evaluate value")
        axL.grid(True)

    @staticmethod
    def plot_comparison(x, y):
        pass

    @staticmethod
    def animate_transition_new(x, y, generation_data, path: str = "", name: str = ""):

        ncols = 1
        nrows = 2

        fig = plt.figure(figsize=(10, 4))
        gs = gridspec.GridSpec(ncols, nrows, width_ratios=(1, 1))
        ax = fig.add_subplot(gs[0, 0])
        ax2 = fig.add_subplot(gs[0, 1:])

        filenames = []
        gif_name = "gif_transion_" + name

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