import sys

input = sys.stdin.readline
t = int(input())
answer = []


def dfs(n):
    if visited[n]:
        return True
    visited[n] = True
    color[n] = 1
    stack = []
    stack.append(n)

    while stack:
        i = stack.pop()
        for j in graph[i]:
            if visited[j]:
                if color[j] == color[i]:
                    return False
                else:
                    continue
            visited[j] = True
            color[j] = color[i] * (-1)
            stack.append(j)

    return True


for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)
    color = [0] * (v + 1)

    for _ in range(e):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    for n in range(1, v + 1):
        if not dfs(n):
            answer.append('NO')
            break
    else:
        answer.append('YES')


for a in answer:
    print(a)
