#!/usr/bin/env python3

"""
Have the function KaprekarsConstant(num) take the num parameter being passed
which will be a 4-digit number with at least two distinct digits. Your program
should perform the following routine on the number: Arrange the digits in
descending order and in ascending order (adding zeroes to fit it to a 4-digit
number), and subtract the smaller number from the bigger number. Then repeat
the previous step. Performing this routine will always cause you to reach a
fixed number: 6174. Then performing the routine on 6174 will always give you
6174 (7641 - 1467 = 6174). Your program should return the number of times this
routine must be performed until 6174 is reached. For example: if num is 3524
your program should return 3 because of the following steps:
(1) 5432 - 2345 = 3087,
(2) 8730 - 0378 = 8352,
(3) 8532 - 2358 = 6174.
"""


def addZeroes(num):
    return int(str(num) + ('0' * (4 - len(str(num)))))


def sortAscend(num):
    return int(''.join(sorted(str(num))))


def sortDescend(num):
    return int(''.join(sorted(str(num), reverse=True)))


def getDiff(num1, num2):
    if num1 >= num2:
        return num1 - num2
    else:
        return num2 - num1


def getConstant(num):
    return getDiff(sortAscend(addZeroes(num)), sortDescend(addZeroes(num)))


def KaprekarsConstant(num):
    c = 0
    while num != 6174:
        num = getConstant(num)
        c += 1
    return c


if __name__ == '__main__':
    print(KaprekarsConstant(6173))
