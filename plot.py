import matplotlib.pyplot as plt
import numpy as np


def find_point_bounds(points):
    smallest_x = points[0][0]
    biggest_x = points[0][0]
    for x, y in points:
        if x < smallest_x:
            smallest_x = x
        elif x > biggest_x:
            biggest_x = x
    return [smallest_x, biggest_x]

def plot_bigO(f, points):
    plt.style.use('dark_background')
    fig, axs = plt.subplots()

    axs.set_xscale('log')

    s_x, b_x = find_point_bounds(points)
    x_axis = np.linspace(s_x, b_x, 500)

    x = []
    y = []
    for (x1, y1)  in points:
        x.append(x1)
        y.append(y1)

    axs.scatter(x, y)
    axs.plot(x_axis, f(x_axis))

    plt.show()

