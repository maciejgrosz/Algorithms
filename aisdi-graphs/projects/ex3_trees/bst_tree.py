#!/usr/bin/python3
"""script that implements Binary Search Tree and Adelson-Velsky-Landis Tree

[TBD]
"""

import random
import time
import gc

from matplotlib import pyplot as plt

# TODO: fix polish comments

class BST:
    '''Binary Search Tree Structure
        obiekt klasy bst reprezentuje węzeł wraz z powiązaniem do dzieci
    '''
    def __init__(self, key = None, val = None):
        self.right = None
        self.left = None
        self.key = key
        self.val = val
        self.size = 1 # TODO

    def __str__(self):
        print("TBD")
    
    def insert(self, key, val = None):
        if not self.key:
            self.key = key
            self.value = val
            return
        
        if self.key == key:
            return

        if key < self.key:
            if self.left:
                self.left.insert(key, val)
                return
            self.left = BST(key = key, val = val)
            self.size = self.size + 1
            return
        
        if self.right:
            self.right.insert(key, val)
            return
        self.right = BST(key, val)
        self.size = self.size + 1
        return

    def search(self, key):
        '''Searches for the key. If key exists, 
           then it returns key and value, otherwise 
           returns False.'''
        if key == self.key:
            return (self.key, self.key)

        if key < self.key:
            if self.left == None:
                return False
            return self.left.search(key)

        if self.right == None:
            return False
        return self.right.search(key)

    def delete(self, key):
        if self == None:
            return self

        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
            return self

        if key > self.key:
            if self.right:
                self.right = self.right.delete(key)
            return self

        if self.right == None:
            return self.left
        
        if self.left == None:
            return self.right

        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.key = min_larger_node.key
        self.right = self.right.delete(min_larger_node.key)
        return self

    def print(self, level = 0):
        if self:
            if self.right:
                self.right.print(level + 1)
            print(' ' * 4 * level + '->', self.key)
            if self.left:
                self.left.print(level + 1)

def list_generator(min_val, max_val, n):
    # print(f'Min: {min_val}, Max: {max_val}, N: {n}')
    return random.sample(range(min_val, max_val + 1), n)

if __name__ == "__main__":
    
    binary_tree = BST(5)

    # TODO generating list with sampling (random.sample(range(1, d), n))
    # inserting numbers in loop
    binary_tree.insert(6)
    binary_tree.insert(1)
    binary_tree.insert(3)
    binary_tree.insert(8)
    binary_tree.insert(10)

    binary_tree.print()
