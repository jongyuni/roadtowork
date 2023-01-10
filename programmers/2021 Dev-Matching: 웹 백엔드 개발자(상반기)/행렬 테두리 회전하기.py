def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns + 1)] for _ in range(rows + 1)]
    num = 1

    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            matrix[row][column] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]
        mini = tmp

        for z in range(x1, x2):
            test = matrix[z + 1][y1]
            matrix[z][y1] = test
            mini = min(mini, test)

        for z in range(y1, y2):
            test = matrix[x2][z + 1]
            matrix[x2][z] = test
            mini = min(mini, test)

        for z in range(x2, x1, -1):
            test = matrix[z - 1][y2]
            matrix[z][y2] = test
            mini = min(mini, test)

        for z in range(y2, y1, -1):
            test = matrix[x1][z - 1]
            matrix[x1][z] = test
            mini = min(mini, test)

        matrix[x1][y1 + 1] = tmp
        answer.append(mini)

    return answer
