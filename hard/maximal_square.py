#!/usr/bin/env python3

testArr = ["0111", "1111", "1111", "1111"]


def convertArr(arr):
    """convert string array into an integer array.

        Input: arr(list)
        Output: result(list)
    """
    result = []
    for i, val in enumerate(arr):
        result.append([])
        for j in val:
            result[i].append(int(j))
    return result


def getMin(matrix, i, j):
    return min(
        matrix[i][j - 1],
        matrix[i - 1][j],
        matrix[i - 1][j - 1]
    ) + 1


def createTable(matrix):
    result = matrix

    i = 1
    while i < len(matrix):
        j = 1
        while j < len(matrix[i]):
            if matrix[i][j] == 1:
                result[i][j] = min(result[i][j - 1],
                                   result[i - 1][j],
                                   result[i - 1][j - 1]
                                   ) + 1

            else:
                result[i][j] = 0
            j += 1
        i += 1

    return result


def MaximalSquare(strArr):
    matrix = convertArr(strArr)
    ansTable = createTable(matrix)

    result = 0
    for i in ansTable:
        maximum = max(i)
        if maximum >= result:
            result = maximum
    return maximum**2


def run(strArr):
    return MaximalSquare(strArr)
    # return createTable(convertArr(strArr))


if __name__ == '__main__':
    print(run(testArr))
