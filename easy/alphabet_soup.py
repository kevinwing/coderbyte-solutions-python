#!/usr/bin/env python3

"""
Challenge:
Have the function AlphabetSoup(str) take the str string parameter
being passed and return the string with the letters in alphabetical
order (ie. hello becomes ehllo). Assume numbers and punctuation
symbols will not be included in the string.

Sample Test Cases:
    Case 1:
        Input:"coderbyte"
        Output:"bcdeeorty"

    Case 2:
        Input:"hooplah"
        Output:"ahhloop"
"""


def alphabetSoup(str):
    return ''.join(sorted(str))


if __name__ == '__main__':
    print(alphabetSoup(input('Text:> ')))
