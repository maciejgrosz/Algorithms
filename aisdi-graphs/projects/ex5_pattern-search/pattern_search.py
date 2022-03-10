from tests import *

from tests import pan_tadeusz_test

def main():
    if boundary_conditions_tests(): print('\nTEST: Boundary conditions tests successful!')
    else: print('TEST: Some boundary conditions tests failed!')

    if random_text_and_pattern_tests(): print('\nTEST: Random text and pattern tests successful!')
    else: print('\nTEST: Random text and pattern tests failed!')

    pan_tadeusz_test()


if __name__ == '__main__':
    main()