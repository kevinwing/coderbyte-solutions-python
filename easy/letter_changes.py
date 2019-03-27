#!/usr/bin/env python3

"""
Challenge
Have the function LetterChanges(str) take the str parameter being passed and
modify it using the following algorithm. Replace every letter in the string
with the letter following it in the alphabet (ie. c becomes d, z becomes a).
Then capitalize every vowel in this new string (a, e, i, o, u) and finally
return this modified string.

Sample Test Cases:
    Case 1:
        Input:"hello*3"
        Output:"Ifmmp*3"

    Case 2:
        Input:"fun times!"
        Output:"gvO Ujnft!"
"""

import string


def letterChanges(sen, offset=1):
    sen = sen.lower()
    alpha = string.ascii_lowercase
    alphaLen = len(alpha)
    newSen = ''

    for char in sen:
        i = alpha.find(char)
        if char.isalpha():
            if i + offset >= alphaLen:
                newSen += chr(ord(char) - (alphaLen - offset))
            else:
                newSen += chr(ord(char) + offset)
        else:
            newSen += char

    for char in newSen:
        if char in 'aeiou':
            newSen = newSen.replace(char, char.upper())

    return newSen


if __name__ == '__main__':
    print(letterChanges(input('> '), offset=5))
