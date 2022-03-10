#!/bin/python3
import time
import sys
import gc
from matplotlib import pyplot as plt

limit = 10000
sys.setrecursionlimit(limit)


def readFile(fileName, n):
    wordlist = []
    with open(fileName, 'r') as file:

        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                wordlist.append(word)
    return wordlist[1:n]


def bubble_sort(our_list):
    # We go through the list as many times as there are elements
    for i in range(len(our_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j+1]:
                # Swap
                our_list[j], our_list[j+1] = our_list[j+1], our_list[j]
    return our_list


def selection_sort(our_list):
    for step in range(len(our_list)):
        min_idx = step

        for i in range(step + 1, len(our_list)):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if our_list[i] < our_list[min_idx]:
                min_idx = i

        # put min at the correct position
        (our_list[step], our_list[min_idx]) = (our_list[min_idx], our_list[step])
    return(our_list)


def quick_sort(our_list):
    elements = len(our_list)

    # Base case
    if elements < 2:
        return our_list

    current_position = 0  # Position of the partitioning element

    for i in range(1, elements):  # Partitioning loop
        if our_list[i] <= our_list[0]:
            current_position += 1
            temp = our_list[i]
            our_list[i] = our_list[current_position]
            our_list[current_position] = temp

    temp = our_list[0]
    our_list[0] = our_list[current_position]
    our_list[current_position] = temp  # Brings pivot to it's appropriate position

    left = quick_sort(our_list[0:current_position])  # Sorts the elements to the left of pivot
    right = quick_sort(our_list[current_position + 1:elements])  # sorts the elements to the right of pivot

    our_list = left + [our_list[current_position]] + right  # Merging everything together
    return our_list


def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


def calculate_time(function, unsorted_list):
    gc_old = gc.isenabled() # garbage collector state
    gc.disable() # disable garbage collector before measuring execution times
    start = time.process_time()
    function(unsorted_list)
    end = time.process_time()
    print(f'Time for {function.__name__}: {end-start}')
    if gc_old: gc.enable() # restore garbage collector initial state
    return end-start


def list_generator():
    qtime = []
    mtime = []
    stime = []
    btime = []
    n_range = range(1000, 10000, 1000)
    for i in n_range:
        unsorted_list_1 = readFile("pan-tadeusz.txt", i)
        unsorted_list_2 = readFile("pan-tadeusz.txt", i)
        unsorted_list_3 = readFile("pan-tadeusz.txt", i)
        unsorted_list_4 = readFile("pan-tadeusz.txt", i)
        qtime.append(calculate_time(quick_sort, unsorted_list_1))
        mtime.append(calculate_time(merge_sort, unsorted_list_3))
        stime.append(calculate_time(selection_sort, unsorted_list_4))
        btime.append(calculate_time(bubble_sort, unsorted_list_2))

    plt.plot(n_range, btime)
    plt.plot(n_range, stime)
    plt.plot(n_range, mtime)
    plt.plot(n_range, qtime)

    # plt.legend(["Merge sort", "Quick sort"])
    plt.legend(["Bubble sort", "Selection sort", "Merge sort", "Quick sort"])
    plt.xlabel("Number of words to sort")
    plt.ylabel("Time execution in seconds")

    plt.show()


list_generator()



