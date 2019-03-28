#!/usr/bin/env python3

"""
Challenge:
Have the function ChessboardTraveling(str) read str which will be a string
consisting of the location of a space on a standard 8x8 chess board with no
pieces on the board along with another space on the chess board. The structure
of str will be the following: "(x y)(a b)" where (x y) represents the position
you are currently on with x and y ranging from 1 to 8 and (a b) represents
some other space on the chess board with a and b also ranging from 1 to 8
where a > x and b > y. Your program should determine how many ways there are
of traveling from (x y) on the board to (a b) moving only up and to the right.

For example:
if str is (1 1)(2 2) then your program should output 2 because there are only
two possible ways to travel from space (1 1) on a chessboard to space (2 2)
while making only moves up and to the right.

Hard challenges are worth 15 points and you are not timed for them.

Sample Test Cases:
    Case 1:
        Input:"(1 1)(3 3)"
        Output:6

    Case 2:
        Input:"(2 2)(4 3)"
        Output:3
"""

routes = [
    [0, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 3, 6, 10, 15, 21, 28, 36],
    [1, 4, 10, 20, 35, 56, 84, 120],
    [1, 5, 15, 35, 70, 126, 210, 330],
    [1, 6, 21, 56, 126, 252, 462, 792],
    [1, 7, 28, 84, 210, 462, 924, 1716],
    [1, 8, 36, 120, 330, 792, 1716, 3432]
]


# def procCoordinates(coords):
#     coords = coords.replace('(', '').replace(')', '').replace(' ', '')
#     return int(coords[0]), int(coords[1]), int(coords[2]), int(coords[3])


def chessboardTraveling(coords):
    arr = coords[1:-1].replace(')(', ' ').split()
    # x, y, a, b = procCoordinates(coords)

    return routes[int(arr[2]) - int(arr[0])][int(arr[3]) - int(arr[1])]


if __name__ == '__main__':
    print(chessboardTraveling(input('enter coordinates:> ')))
