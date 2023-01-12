from collections import deque


def ispressed(x, y, n, arr):
    pivot = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != pivot:
                return -1
    else:
        if pivot:
            return 1
        else:
            return 0


def solution(arr):
    answer = []
    zero = 0
    one = 0
    start = deque([(0, 0, len(arr))])

    while start:
        x, y, n = start.popleft()
        s = ispressed(x, y, n, arr)
        if s == 1:
            one += 1
        elif s == 0:
            zero += 1
        elif s < 0:
            start.append((x, y, n // 2))
            start.append((x, y + n // 2, n // 2))
            start.append((x + n // 2, y, n // 2))
            start.append((x + n // 2, y + n // 2, n // 2))

    answer.append(zero)
    answer.append(one)
    return answer
