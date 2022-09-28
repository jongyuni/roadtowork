import sys

N, M = map(int, sys.stdin.readline().split())
table = [[0] * (N+1)]
D = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp = [0] + tmp
    table.append(tmp)

for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + table[i][j]

for _ in range(M):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    print(D[X2][Y2] - D[X1-1][Y2] - D[X2][Y1-1] + D[X1-1][Y1-1])
