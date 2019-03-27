#!/usr/bin/env python3

"""
Challenge:
Have the function LetterCapitalize(str) take the str parameter being passed
and capitalize the first letter of each word. Words will be separated by only
one space.

Sample Test Cases:
    Case 1:
        Input:"hello world"
        Output:"Hello World"

    Case 2:
        Input:"i ran there"
        Output:"I Ran There"
"""

testString = 'hello world!'


def letterCapitalize(sen):
    return sen.title()


if __name__ == '__main__':
    print(letterCapitalize(testString))
