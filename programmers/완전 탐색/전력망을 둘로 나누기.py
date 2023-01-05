import sys


def dfs(i, visited, table):
    visited[i] = True
    cnt = 1

    for j in table[i]:
        if not visited[j]:
            cnt += dfs(j, visited, table)

    return cnt


def solution(n, wires):
    answer = int(sys.maxsize)

    for i in range(n - 1):
        table = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        for j in range(n - 1):
            if i == j:
                continue
            s, e = wires[j]
            table[s].append(e)
            table[e].append(s)
        x, y = wires[i]
        a = dfs(x, visited, table)
        b = dfs(y, visited, table)

        answer = min(answer, abs(a - b))

    return answer
