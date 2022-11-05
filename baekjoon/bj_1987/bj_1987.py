import sys

input = sys.stdin.readline
R, C = map(int, input().split())
visited = [0] * 26
alpha = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(R)]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
answer = 0


def dfs(i, j, count):
    global answer
    answer = max(count, answer)
    for pi, pj in directions:
        ni = i + pi
        nj = j + pj
        if 0 <= ni < R and 0 <= nj < C and visited[alpha[ni][nj]] != 1:
            visited[alpha[ni][nj]] = 1
            dfs(ni, nj, count + 1)
            visited[alpha[ni][nj]] = 0


visited[alpha[0][0]] = 1
dfs(0, 0, 1)
print(answer)
