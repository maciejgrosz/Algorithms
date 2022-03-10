#!/usr/bin/python3
"""program that takes in text files and carries out different sort methods

All algorithms works ascending [TBD]
"""

import sys
import argparse

import timeit
import time
import gc

import matplotlib.pyplot as plt

def bubble_sort(list_to_sort):
    '''Bubble sort for array'''
    sorted_list = list_to_sort
    list_length = len(list_to_sort)
    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

def selection_sort(list_to_sort):
    '''Selection sort for array'''
    sorted_list = list_to_sort
    list_length = len(list_to_sort)
    for i in range(list_length-1):
        min_id = i
        for j in range(i+1, list_length-1):
            if sorted_list[min_id] > sorted_list[j]:
                min_id = j
        sorted_list[i], sorted_list[min_id] = sorted_list[min_id], sorted_list[i]
    return sorted_list

def merge(arr1, arr2):
    merged_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i+=1
        else:
            merged_arr.append(arr2[j])
            j+=1
    while i < len(arr1):
        merged_arr.append(arr1[i])
        i+=1
    while j < len(arr2):
        merged_arr.append(arr2[j])
        j+=1
    return merged_arr

def merge_sort(list_to_sort):
    '''Merge sort for array'''
    sorted_list = list_to_sort
    list_length = len(list_to_sort)

    if list_length == 1:
        return sorted_list
    else:
        mid = int(list_length/2)
        sorted_list = merge(merge_sort(sorted_list[0:mid]), merge_sort(sorted_list[mid:]))

    return sorted_list

def partition(list_to_partition):
    '''Partitioning for quick sort. Returns partitioned list and middle index'''
    partition_list = list_to_partition
    list_length = len(list_to_partition)
    i, j = 1, list_length-1
    pivot = partition_list[0]
    while True:
        while partition_list[i] <= pivot:
            i+=1
            if i >= list_length-1: break
        while partition_list[j] >= pivot: 
            j-=1
            if j == 0: break
        if i >= j: break
        partition_list[i], partition_list[j] = partition_list[j], partition_list[i]
    partition_list[j], partition_list[0] = partition_list[0], partition_list[j]
    return partition_list, j

def quick_sort(list_to_sort):
    '''Quick sort for array'''
    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        partitioned_list, mid = partition(list_to_sort)
        arr1 = quick_sort(partitioned_list[:mid+1])
        arr2 = quick_sort(partitioned_list[mid+1:])
    return arr1 + arr2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Carries out different sort methods on text file.")
    parser.add_argument('file_name', metavar="FILE_NAME", type=argparse.FileType('r'),
                        help='text file name to sort')
    args = parser.parse_args()

    sentences_words_list = list(map(lambda x: x.split(), args.file_name.readlines()))
    words_list = [ x for y in sentences_words_list for x in y]

    gc_old = gc.isenabled() # garbage collector state
    gc.disable() # disable garbage collector before measuring execution times

    bs_times = []
    ss_times = []
    ms_times = []
    qs_times = []

    max_n = 10000
    step = 1000
    words_quantities_range = range(step, max_n+1, step)

    # default recursion limit for python interpreter is 1000, if it is not enough increase the limit
    limit = 1000
    sys.setrecursionlimit(limit)

    for n in words_quantities_range: # +1 for inclusive range

        print("n = ", n)

        start = time.process_time()
        bubble_sort(words_list[0:n])
        stop = time.process_time()
        bs_times.append(stop - start)
        print('Time execution in seconds for "bubble sort":', bs_times[-1])

        start = time.process_time()
        selection_sort(words_list[0:n])
        stop = time.process_time()
        ss_times.append(stop - start)
        print('Time execution in seconds for "selection sort":', ss_times[-1])

        start = time.process_time()
        m = merge_sort(words_list[0:n])
        stop = time.process_time()
        ms_times.append(stop - start)
        print('Time execution in seconds for "merge sort":', ms_times[-1])

        start = time.process_time()
        quick_sort(words_list[0:n])
        stop = time.process_time()
        qs_times.append(stop - start)
        print('Time execution in seconds for "quick sort":', qs_times[-1])

    plt.plot(words_quantities_range, bs_times)
    plt.plot(words_quantities_range, ss_times)
    plt.plot(words_quantities_range, ms_times)
    plt.plot(words_quantities_range, qs_times)
    
    # plt.legend(["Merge sort", "Quick sort"])
    plt.legend(["Bubble sort", "Selection sort", "Merge sort", "Quick sort"])
    plt.xlabel("Number of words to sort")
    plt.ylabel("Time execution in seconds")
    
    plt.show()

    if gc_old: gc.enable() # restore garbage collector initial state

    # Time execution with timeit [TBD]
    # All below tries are wrong
    # Checkout: https://www.geeksforgeeks.org/timeit-python-examples/
    # timeit.timeit(stmt=selection_sort([]))
    # timeit.timeit(stmt=merge_sort([]))
    # timeit.timeit(stmt=quick_sort)