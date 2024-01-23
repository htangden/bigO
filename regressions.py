
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