import numpy as np
from random import *
from functions import *


def remove_element(array, i):
    return array[:i] + array[i+1:(len(array))]

def brute_sort(array): 
    output_arr = []
    for i in range(len(array)):
        smallest = np.Infinity
        for j in range(len(array)):
            if array[j] < smallest:
                smallest_index = j
                smallest = array[j]
        output_arr.append(array[smallest_index])
        array = remove_element(array, smallest_index)
    return output_arr

def brute_sort_multiple(array1, array2):
    output_arr1 = []
    output_arr2 = []
    for i in range(len(array1)):
        smallest = np.Infinity
        for j in range(len(array1)):
            if array1[j] < smallest:
                smallest_index = j
                smallest = array1[j]
        output_arr1.append(array1[smallest_index])
        output_arr2.append(array2[smallest_index])
        array1 = remove_element(array1, smallest_index)
        array2 = remove_element(array2, smallest_index)
    return output_arr1, output_arr2


