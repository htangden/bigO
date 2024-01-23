from functions import *
from regressions import *
from plot import *
import numpy as np


arr = [1, 100, 1000, 10000, 100000]

points = np.vstack((arr, normalize_array(multiple_testing(amount_of_orders, arr)))).T # most readable line of code ever :))

degress_of_polynomial = [0.5, 1, 2, 3]
functions = []

for degree in degress_of_polynomial:
    functions.append(poly_regression(degree, points))

index_of_lowest_cost = 0
lowest_cost = np.Infinity
for i, function in enumerate(functions):
    cost = calculate_cost(function, points)
    print(cost)
    if cost < lowest_cost:
        index_of_lowest_cost = i


plot_bigO(functions[index_of_lowest_cost], points)
