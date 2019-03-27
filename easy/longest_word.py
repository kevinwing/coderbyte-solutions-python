#!/usr/bin/env python3

"""
Challenge:
    Have the function LongestWord(sen) take the sen parameter being passed and
    return the largest word in the string. If there are two or more words that
    are the same length, return the first word from the string with that
    length. Ignore punctuation and assume sen will not be empty.

Sample Test Cases:

    Case 1:
        Input:"fun&!! time"

        Output:"time"

    Case 2:
        Input:"I love dogs"

        Output:"love"
"""

import string


def longestWord(sen):
    alphabet = string.ascii_letters + string.digits
    for char in sen:
        if char not in alphabet:
            sen = sen.replace(char, ' ')

    word_list = sen.split()
    sen = word_list[0]
    for word in word_list:
        if len(word) > len(sen):
            sen = word
    return sen


if __name__ == '__main__':
    print(longestWord(input('Text here:> ')))
