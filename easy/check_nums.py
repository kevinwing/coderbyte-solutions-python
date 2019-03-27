#!/usr/bin/env python3

"""
Challenge:
Have the function CheckNums(num1,num2) take both parameters being passed and
return the string true if num2 is greater than num1, otherwise return the
string false. If the parameter values are equal to each other then return the
string -1.

Sample Test Cases:
    Case 1:
        Input:3 & num2 = 122
        Output:"true"

    Case 2:
        Input:67 & num2 = 67
        Output:"-1"
"""


def checkNums(num1, num2):
    if num1 == num2:
        return -1
    elif num1 < num2:
        return 'true'
    else:
        return 'false'


if __name__ == '__main__':
    print(checkNums(int(input('1st Num:> ')), int(input('2nd Num:> '))))
