#!/usr/bin/python3
import random
import time
import gc

from matplotlib import pyplot as plt

from bst_tree import BST, list_generator
from avl_tree import AVL

if __name__ == "__main__":
    
    number_of_nodes = range(1000, 10001, 1000)

    min_val = 1
    max_val = 1000

    bst_creating_time = []
    bst_searching_time = []
    bst_deleting_time = []

    avl_creating_time = []
    avl_searching_time = []
    avl_deleting_time = []

    gc_old = gc.isenabled() # garbage collector state
    gc.disable() # disable garbage collector before measuring execution times

    for i in number_of_nodes:
        bst_tree = BST()
        avl_tree = AVL()

        # keys_list = list_generator(min_val, max_val, i)
        keys_list = list_generator(min_val, i, i)
        start = time.process_time()
        for j in keys_list:
            bst_tree.insert(j)
        stop = time.process_time()
        bst_creating_time.append(stop-start)
        print(f'Czas tworzenia {i} elementów drzewa bst: {bst_creating_time[-1]}')

        start = time.process_time()
        for j in keys_list:
            avl_tree.insert(j)
        stop = time.process_time()
        avl_creating_time.append(stop-start)
        print(f'Czas tworzenia {i} elementów drzewa avl: {avl_creating_time[-1]}')

        start = time.process_time()
        for j in keys_list:
            bst_tree.search(j)
        stop = time.process_time()
        bst_searching_time.append(stop-start)
        print(f'Czas wyszukiwania {i} elementów drzewa bst: {bst_searching_time[-1]}')

        start = time.process_time()
        for j in keys_list:
            avl_tree.find(j)
        stop = time.process_time()
        avl_searching_time.append(stop-start)
        print(f'Czas wyszukiwania {i} elementów drzewa: {avl_searching_time[-1]}')

        start = time.process_time()
        for j in keys_list:
            bst_tree.delete(j)
        stop = time.process_time()
        bst_deleting_time.append(stop-start)
        print(f'Czas usuwania {i} elementów drzewa: {bst_deleting_time[-1]}')

        start = time.process_time()
        for j in keys_list:
            avl_tree.remove(j)
        stop = time.process_time()
        avl_deleting_time.append(stop-start)
        print(f'Czas usuwania {i} elementów drzewa: {avl_deleting_time[-1]}')

    if gc_old: gc.enable() # restore garbage collector initial state


    plt.figure(1)
    plt.plot(number_of_nodes, bst_creating_time)
    plt.plot(number_of_nodes, avl_creating_time)
    plt.title("Tworzenie drzewa")
    plt.legend(["BST", "AVL"])
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas")

    plt.figure(2)
    plt.plot(number_of_nodes, bst_searching_time)
    plt.plot(number_of_nodes, avl_searching_time)
    plt.title("Szukanie elementów")
    plt.legend(["BST", "AVL"])
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas")

    plt.figure(3)
    plt.plot(number_of_nodes, bst_deleting_time)
    plt.plot(number_of_nodes, avl_deleting_time)
    plt.title("Usuwanie elementów")
    plt.legend(["BST", "AVL"])
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas")
    
    plt.show()