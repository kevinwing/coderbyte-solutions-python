#!/usr/bin/env python3

"""
Challenge:
Have the function SimpleAdding(num) add up all the numbers from 1 to num.
For example: if the input is 4 then your program should return 10 because
1 + 2 + 3 + 4 = 10. For the test cases, the parameter num will be any number
from 1 to 1000.

Sample Test Cases:
    Case 1:
        Input:12
        Output:78

    Case 2:
        Input:140
        Output:9870
"""


def simpleAdding(num):

    if num == 1:
        return num
    else:
        return num + simpleAdding(num - 1)


if __name__ == '__main__':
    print(simpleAdding(int(input('Number:> '))))
