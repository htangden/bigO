from timing import *



def amount_of_orders(n):
    count = 1
    for i in range(n):
        count *= (i+1)
    return count

def multiple_testing(f, arr):
    times = []
    for n in arr:
        times.append(test_time(f, n))
    return times

def normalize_array(arr):
    product = []
    for a in arr:
        product.append(a/arr[0])
    return product

def sci_not(number):
    count = 0
    if number > 1:
        while number > 10:
            count += 1
            number /= 10
    else:
        while number < 1:
            count -= 1
            number *= 10
    
    prefix = f"{number:.2f}"
    suffix = f"e{count}"
    return prefix + suffix