from functions import *
from regressions import *
from plot import *
import numpy as np

bigO_func = amount_of_orders 

test_points = 8
test_base = 5

testing_values = []

for i in range(test_points):
    testing_values.append(test_base**i)

points = np.vstack((testing_values, normalize_array(multiple_testing(bigO_func, testing_values)))).T # most readable line of code ever :))

functions = [sqrt, linear, quadratic, cubic, log, xlog]
function_names = ["x^0.5", "x", "x^2", "x^3", "log(x)", "xlog(x)"]

index_of_lowest_cost = 0
lowest_cost = np.Infinity
costs = []

for i, function in enumerate(functions):
    functions[i] = simple_regression(points, function)

    costs.append(calculate_cost(functions[i], points))
    if costs[i] < lowest_cost:
        index_of_lowest_cost = i
    
print(costs)

plot_bigO(functions, function_names, costs, points)