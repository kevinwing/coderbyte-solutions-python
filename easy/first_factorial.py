#!/usr/bin/env python3

"""
Challenge:
Have the function FirstFactorial(num) take the num parameter being passed and
return the factorial of it. For example: if num = 4, then your program should
return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1
and 18 and the input will always be an integer.

Sample Test Cases:
    Case 1:
        Input:4
        Output:24

    Case 2:
        Input:8
        Output:40320
"""


def firstFactorial(number):
    if number == 1:
        return 1
    else:
        return number * firstFactorial(number - 1)


if __name__ == "__main__":
    firstFactorial(input('Enter Number:> '))
