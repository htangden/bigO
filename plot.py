import matplotlib.pyplot as plt
import numpy as np
from functions import *


def find_point_bounds(points):
    smallest_x = points[0][0]
    biggest_x = points[0][0]
    for x, y in points:
        if x < smallest_x:
            smallest_x = x
        elif x > biggest_x:
            biggest_x = x
    return [smallest_x, biggest_x]

def plot_bigO(functions, costs, points):
    plt.style.use('dark_background')
    fig, axs = plt.subplots(nrows=int(len(functions)/2), ncols=2, figsize=(10, 7))
    s_x, b_x = find_point_bounds(points)
    x_axis = np.linspace(s_x, b_x, 500)

    x = []
    y = []
    for (x1, y1)  in points:
        x.append(x1)
        y.append(y1)

    for i, f in enumerate(functions):
        row = int(i%(len(functions)/2))
        col = int(i/(len(functions)/2))
        axs[row][col].scatter(x, y, color='magenta')
        axs[row][col].plot(x_axis, f[0](x_axis), color='cyan')
        axs[row][col].set_title(f'{f[1]} - {sci_not(costs[i])}')

    fig.subplots_adjust(hspace=0.5)
    plt.show()

