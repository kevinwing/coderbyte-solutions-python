#!/usr/bin/env python3

"""
Challenge:
Have the function FirstReverse(str) take the str parameter being passed and
return the string in reversed order. For example: if the input string is
"Hello World and Coders" then your program should return the string sredoC
dna dlroW olleH.

Sample Test Cases:
    Case 1:
        Input:"coderbyte"
        Output:"etybredoc"

    Case 2:
        Input:"I Love Code"
        Output:"edoC evoL I"
"""


def firstReverse(inputStr):
    return inputStr[::-1]


if __name__ == '__main__':
    firstReverse(input('Text:> '))
