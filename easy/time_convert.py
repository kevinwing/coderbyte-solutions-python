#!/usr/bin/env python3

"""
Challenge:
Have the function TimeConvert(num) take the num parameter being passed and
return the number of hours and minutes the parameter converts to
(ie. if num = 63 then the output should be 1:3). Separate the number of hours
and minutes with a colon.

Sample Test Cases:
    Case 1:
        Input:126
        Output:"2:6"

    Case 2:
        Input:45
        Output:"0:45"
"""


def timeConvert(num):
    return str(num // 60) + ':' + str(num % 60)


if __name__ == '__main__':
    print(timeConvert(int(input('Minutes:> '))))
