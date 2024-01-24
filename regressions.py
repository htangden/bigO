import numpy as np

def calculate_cost(f, points):
    cost_sum = 0
    for (x, y) in points:
        cost_sum += (y - f(x))**2
    return cost_sum

def poly_regression(b, points):
    sum_of = {
        "yx**b" : 0,
        "x**2b" : 0
    }
    
    for (x, y) in points:
        sum_of["yx**b"] += y*(x**b)
        sum_of["x**2b"] += x**(2*b)

    a = (1/sum_of["x**2b"])*(sum_of["yx**b"])

    def f(x):
        return a*(x**b)

    return f

def simple_regression(points, g): # scales any given function g so that the quadratic cost i minimized
    sum_of = {
        "yg": 0,
        "g**2": 0
    }

    for (x, y) in points:
        sum_of["yg"] += y * g(x)
        sum_of["g**2"] += (g(x))**2
    
    a = sum_of["yg"]/sum_of["g**2"]

    def f(x):
        return a * g(x)

    return f

def quadratic(x):
    return x**2

def sqrt(x):
    return x**(0.5)

def cubic(x):
    return x**3

def linear(x):
    return x

def log(x):
    return np.log(x)

def xlog(x):
    return x * np.log(x)