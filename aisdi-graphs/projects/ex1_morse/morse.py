#!/usr/bin/python3
"""program, which converts text file to a morse encoding

It ignores any aplhanumeric signs, except 
letters (which are later morse encoded).
For usage type: ./morse.py --help
"""

import sys
import argparse

def main():
    '''Main function, which opens dictionary file 
    and runs morse conversion on specified text file.'''
    morse_dictionary = {}
    with open("morse_dict.txt", "r") as file:
        for line in file:
            (key, val) = line.split()
            morse_dictionary[key] = val

    word_end_slash = False
    for line in args.file_name:
        for letter in line.upper():
            if letter == " " and word_end_slash:
                print("/", end=" ")
                word_end_slash = False
                continue
            if letter in morse_dictionary.keys():
                print(morse_dictionary[str(letter)], end=" ")
                word_end_slash = True
            else:
                word_end_slash = False
        print()     

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Converts text file to Morse alphabet.')
    parser.add_argument('file_name', metavar="FILE_NAME", type=argparse.FileType('r'),
                        help='text file name to convert')
    args = parser.parse_args()
    main()