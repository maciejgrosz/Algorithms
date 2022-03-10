from search_pattern_algorithms import *
import random

def boundary_conditions_tests():
    success = 1

    print('\nTEST: Empty pattern:')
    pattern = ''
    txt = 'abc'

    if naive_alg(pattern, txt) == []:
        print('Naive succeded empty pattern') 
    else: 
        print('Naive failed empty pattern')
        success = 0

    if KMP_alg(pattern, txt) == []:
        print('KMP succeded empty pattern')
    else: 
        print('KMP failed empty pattern')
        success = 0

    if RK_alg(pattern, txt) == []:
        print('RK succeded empty pattern')
    else:
        print('RK failed empty pattern')
        success = 0

    print('\nTEST: Empty strings:')
    pattern = ''
    txt = ''

    if naive_alg(pattern, txt) == []:
        print('Naive succeded empty strings') 
    else: 
        print('Naive failed empty strings')
        success = 0

    if KMP_alg(pattern, txt) == []:
        print('KMP succeded empty strings')
    else: 
        print('KMP failed empty strings')
        success = 0

    if RK_alg(pattern, txt) == []:
        print('RK succeded empty strings')
    else:
        print('RK failed empty strings')
        success = 0

    print('\nTEST: Text equals pattern:')
    pattern = 'abc'
    txt = 'abc'

    if naive_alg(pattern, txt) == [0]:
        print('Naive succeded text equals pattern') 
    else: 
        print('Naive failed text equals pattern')
        success = 0

    if KMP_alg(pattern, txt) == [0]:
        print('KMP succeded text equals pattern')
    else: 
        print('KMP failed text equals pattern')
        success = 0

    if RK_alg(pattern, txt) == [0]:
        print('RK succeded text equals pattern')
    else:
        print('RK failed text equals pattern')
        success = 0

    print('\nTEST: Pattern longer than text:')
    pattern = 'abcd'
    txt = 'abc'

    if naive_alg(pattern, txt) == []:
        print('Naive succeded pattern longer than text') 
    else: 
        print('Naive failed pattern longer than text')
        success = 0

    if KMP_alg(pattern, txt) == []:
        print('KMP succeded pattern longer than text')
    else: 
        print('KMP failed pattern longer than text')
        success = 0

    if RK_alg(pattern, txt) == []:
        print('RK succeded pattern longer than text')
    else:
        print('RK failed pattern longer than text')
        success = 0

    print('\nTEST: Pattern does not exist in text:')
    pattern = 'abc'
    txt = 'afbscadfcxz'

    if naive_alg(pattern, txt) == []:
        print('Naive succeded pattern does not exist in text') 
    else: 
        print('Naive failed pattern does not exist in text')
        success = 0

    if KMP_alg(pattern, txt) == []:
        print('KMP succeded pattern does not exist in text')
    else: 
        print('KMP failed pattern does not exist in text')
        success = 0

    if RK_alg(pattern, txt) == []:
        print('RK succeded pattern does not exist in text')
    else:
        print('RK failed pattern does not exist in text')
        success = 0

    print('\nTEST: One match:')
    pattern = 'abc'
    txt = '12eab12abc3av'

    if naive_alg(pattern, txt) == [7]:
        print('Naive succeded one match')  
    else:
        print('Naive failed one match')
        success = 0

    if KMP_alg(pattern, txt) == [7]:
        print('KMP succeded one match')  
    else: 
        print('KMP failed one match')
        success = 0

    if RK_alg(pattern, txt) == [7]:
        print('RK succeded one match')
    else: 
        print('RK failed one match')
        success = 0

    print('\nTEST: Multiple match:')
    pattern = 'abc'
    txt = '12eabc2abc3av'

    if naive_alg(pattern, txt) == [3,7]:
        print('Naive succeded multiple match') 
    else: 
        print('Naive failed multiple match')
        success = 0

    if KMP_alg(pattern, txt) == [3,7]:
        print('KMP succeded multiple match')
    else: 
        print('KMP failed multiple match')
        success = 0

    if RK_alg(pattern, txt) == [3,7]:
        print('RK succeded multiple match')
    else:
        print('RK failed multiple match')
        success = 0

    return success

def random_text_and_pattern_tests():
    text_length = 20
    pattern_length = random.randint(1, 20)

    text = ''
    pattern = ''

    for _ in range(text_length):
        text += chr(random.randint(65,66)) # ['A', 'B']

    for _ in range(pattern_length):
        pattern += chr(random.randint(65,66))

    # text = 'BAAAAAAABBAAAAABBABB'
    # pattern = 'AAA'

    print(text)
    print(pattern)

    na = naive_alg(pattern, text)
    ka = KMP_alg(pattern, text)
    ra = RK_alg(pattern, text)

    print(f'na: {na}, ka: {ka}, ra: {ra}')

    if na == ka == ra:
        return 1
    return 0

import time
import gc

import matplotlib.pyplot as plt

def pan_tadeusz_test():

    f = open('pan-tadeusz.txt', 'r')
    whole_file_text = f.read()
    sentences_words_list = list(map(lambda x: x.split(), whole_file_text.split('\n')))
    words_list = [ x for y in sentences_words_list for x in y]
    f.close()

    gc_old = gc.isenabled() # garbage collector state
    gc.disable() # disable garbage collector before measuring execution times

    naive_times = []
    kmp_times = []
    rk_times = []

    # words_quantities_range = range(100, 1001, 100)
    words_quantities_range = range(1, 20)

    for n in words_quantities_range:
        start = time.process_time()
        for i in range(n):
            naive_alg(words_list[i], whole_file_text)
        stop = time.process_time()
        naive_times.append(stop - start)

        start = time.process_time()
        for i in range(n):
            KMP_alg(words_list[i], whole_file_text)
        stop = time.process_time()
        kmp_times.append(stop - start)

        start = time.process_time()
        for i in range(n):
            RK_alg(words_list[i], whole_file_text)
        stop = time.process_time()
        rk_times.append(stop - start)

    plt.plot(words_quantities_range, naive_times)
    plt.plot(words_quantities_range, kmp_times)
    plt.plot(words_quantities_range, rk_times)
    
    plt.legend(["Naive algorithm", "KMP algorithm", "RK algorithm"])
    plt.xlabel("Number of words to search for")
    plt.ylabel("Time execution in seconds")
    
    plt.show()

    if gc_old: gc.enable() # restore garbage collector initial state

