from time import *

def test_time(f, n):
    a = time()
    f(n)
    b = time()
    return b - a