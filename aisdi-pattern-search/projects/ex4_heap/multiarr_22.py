import math
from io import StringIO

import numpy as np

import time
import gc

import matplotlib.pyplot as plt

class Heap:
    def __init__(self, d):
        self.d = d # arnosc kopca
        self.items = []

    def parent(self, k):
        return (k - 1) // self.d

    def child(self, k, index): # indeks 1,2 dla kopca binarnego, 1,2,3 dla d=3
        return self.d * k + index

    def get_top(self):
        return self.items[0]

    def up_heap(self, k):
        while k != 0 and self.items[self.parent(k)] > self.items[k]:
            # print(f"Child {self.items[k]} and parent {self.items[self.parent(k)]} switched!")
            self.items[k], self.items[self.parent(k)] = self.items[self.parent(k)], self.items[k]
            k = self.parent(k)

    def down_heap(self, k):  # sinking down -> when k is bigger than child
        while self.child(k,1) < len(self.items):
            j = self.child(k,1)
            m = 0
            for i in range(self.d-1, 0, -1):
                if j + i < len(self.items) and self.items[j + i] < self.items[j+m]:
                    m = i
            j += m
            if self.items[k] < self.items[j]:
                break
            self.items[k], self.items[j] = self.items[j], self.items[k]
            k = j
        
    # def repair_tree(self, k=0):
    #     j = self.child(k,1)
    #     for i in range(0, self.d):
    #         if (j+i<len(self.items)):
    #             self.repair_tree(j+i)
    #             self.down_heap(j+i)
    #     self.down_heap(0)

    def push(self, element):
        self.items.append(element)
        self.up_heap(len(self.items) - 1)

    def pop(self):  # delete the smallest element of heap and return it
        root = self.items[0]
        self.items[0] = self.items[len(self.items) - 1]
        self.items = self.items[:-1]
        self.down_heap(0)
        return root

    def make_heap(self, items):  # This function runs a loop starting from the last non-leaf node all the way up to the root node
        self.items = items
        a = (len(self.items) - 2) // self.d
        while a >= 0:
            self.down_heap(a)
            a -= 1
        return self.items

    def show_tree(self, total_width=60, fill=' '):
        """Pretty-print a tree.
        total_width depends on your input size"""
        output = StringIO()
        last_row = -1
        for i, n in enumerate(self.items):
            if i:
                thres = self.d
                r = 1
                while (i > thres):
                    r += 1
                    thres += thres**r 
                row = r
                #row = int(math.floor(math.log(i + 2, self.d)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = self.d ** row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print(output.getvalue())
        print('-' * total_width)




def main():

    heap = Heap(2)
    for number in np.random.randint(1, 26, 10):
        heap.push(number)
    heap.show_tree()
    print(heap.items)

    # heap2 = Heap(3)
    # for number in np.random.randint(1, 100, 30):
    #     heap2.items.append(number)
    # heap2.show_tree(total_width=120)

    # heap2.repair_tree()
    # heap2.show_tree(total_width=120)

    heap3 = Heap(3)
    numbers = []
    for number in np.random.randint(1, 26, 20):
        numbers.append(number)
    print(numbers)
    heap3.make_heap(numbers)
    heap3.show_tree(total_width=140)

    # Tests:
    sample_list = np.random.randint(1, 300000, 100000)
    number_of_elements = range(10000, 100001, 10000)

    creating_times = []
    creating_time = []
    deleting_time = []
    deleting_times = []


    gc_old = gc.isenabled() # garbage collector state
    gc.disable() # disable garbage collector before measuring execution times
    heap_list = []
    # for every heap
    for x in range(2, 5):
        creating_time = []
        deleting_time = []
        # Creating Heaps
        for n in number_of_elements:
            test_heap = Heap(x)
            list_for_heap = sample_list[:n]
            start = time.process_time()
            test_heap.make_heap(list_for_heap)
            stop = time.process_time()
            creating_time.append(stop-start)
            heap_list.append(test_heap)


            start_d = time.process_time()
            while len(test_heap.items) != 0:
                test_heap.pop()
            stop_d = time.process_time()

            deleting_time.append(stop_d - start_d)
        creating_times.append(creating_time)
        deleting_times.append(deleting_time)


    if gc_old: gc.enable() # restore garbage collector initial state
    
    plt.figure(1)
    plt.plot(number_of_elements, creating_times[0])
    plt.plot(number_of_elements, creating_times[1])
    plt.plot(number_of_elements, creating_times[2])
    plt.title("Tworzenie kopca")
    plt.legend(["2-arr heap", "3-arr heap", "4-arr heap"])
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas")

    plt.figure(2)
    plt.plot(number_of_elements, deleting_times[0])
    plt.plot(number_of_elements, deleting_times[1])
    plt.plot(number_of_elements, deleting_times[2])
    plt.title("Usuwanie elementów")
    plt.legend(["2-arr heap", "3-arr heap", "4-arr heap"])
    plt.xlabel("Liczba elementów")
    plt.ylabel("Czas")
    
    plt.show()


if __name__ == '__main__':
    raise SystemExit(main())
