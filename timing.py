from time import *
from random import *

def generate_random_arr(n):
    output_arr = []
    for i in range(n):
        output_arr.append(randint(1, 1000))
    return output_arr

def test_time(f, n):
    arr = generate_random_arr(n)
    a = time()
    f(arr)
    b = time()
    return b - a