#!/usr/bin/env python3

"""
Challenge:
Have the function SimpleSymbols(str) take the str parameter being passed and
determine if it is an acceptable sequence by either returning the string true
or false. The str parameter will be composed of + and = symbols with several
letters between them (ie. ++d+===+c++==a) and for the string to be true each
letter must be surrounded by a + symbol. So the string to the left would be
false. The string will not be empty and will have at least one letter.

Sample Test Cases:
    Case 1:
        Input:"+d+=3=+s+"
        Output:"true"

    Case 2:
        Input:"f++d+"
        Output:"false"
"""


def simpleSymbols(word):

    if word[0].isalpha() or word[-1].isalpha():
        return 'false'

    i = 1
    while i < len(word):
        if word[i].isalpha():
            if word[i - 1] != '+' or word[i + 1] != '+':
                return 'false'

        i += 1

    return 'true'


if __name__ == '__main__':
    simpleSymbols(input('Word:> '))
