from collections import deque

N = int(input())
que = deque(map(int, input().split()))
calc = list(map(int, input().split()))
max_value = -999999999
min_value = 999999999

def dfs(que, total, pl, mi, mu, di, M):
    global max_value
    global min_value
    if M == N-1:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return
    if pl:
        dfs(que, total+que[M+1], pl-1, mi, mu, di, M+1)
    if mi:
        dfs(que, total-que[M+1], pl, mi-1, mu, di, M+1)
    if mu:
        dfs(que, total*que[M+1], pl, mi, mu-1, di, M+1)
    if di:
        dfs(que, int(total / que[M+1]), pl, mi, mu, di-1, M+1)

    return

dfs(que, que[0], calc[0], calc[1], calc[2], calc[3], 0)

print(max_value)
print(min_value)


