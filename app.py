from functions import *
from regressions import *
from plot import *
from sorting import *
import numpy as np

bigO_func = brute_sort 

test_points = 10
test_base = 2

testing_values = []

for i in range(test_points):
    testing_values.append(test_base**i)

points = np.vstack((testing_values, normalize_array(multiple_testing(bigO_func, testing_values)))).T # most readable line of code ever :))

functions = [[sqrt, "x^0.5"], [linear, "x"], [quadratic, "x^2"], [cubic, "x^3"], [log, "log(x)"], [xlog, "xlog(x)"]]

costs = []

for i, function in enumerate(functions):
    functions[i][0] = simple_regression(points, function[0])
    costs.append(calculate_cost(functions[i][0], points))


costs, functions = brute_sort_multiple(costs, functions)

print(costs, functions)

plot_bigO(functions, costs, points)


