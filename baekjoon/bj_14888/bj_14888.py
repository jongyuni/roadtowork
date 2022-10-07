from collections import deque

N = int(input())
que = deque(map(int, input().split()))
calc = list(map(int, input().split()))
max_value = -999999999
min_value = 999999999

def dfs(que:deque, calc:list, M:int):
    global max_value
    global min_value
    if M == N-1:
        a = que[0]
        max_value = max(max_value, a)
        min_value = min(min_value, a)
        return
    x = que.popleft()
    y = que.popleft()

    if calc[0] > 0:
        plus = x + y
        calc[0] -= 1
        tmp = deque()
        tmp.append(plus)
        tmp += que
        dfs(tmp, calc, M + 1)
        calc[0] += 1

    if calc[1] > 0:
        minus = x - y
        calc[1] -= 1
        tmp = deque()
        tmp.append(minus)
        tmp += que
        dfs(tmp, calc, M + 1)
        calc[1] += 1

    if calc[2] > 0:
        multiple = x * y
        calc[2] -= 1
        tmp = deque()
        tmp.append(multiple)
        tmp += que
        dfs(tmp, calc, M + 1)
        calc[2] += 1

    if calc[3] > 0:
        if x < 0 and y > 0:
            divide = -(abs(x) // y)
        else:
            divide = x // y
        calc[3] -= 1
        tmp = deque()
        tmp.append(divide)
        tmp += que
        dfs(tmp, calc, M + 1)
        calc[3] += 1

    que.appendleft(y)
    que.appendleft(x)

    return

dfs(que, calc, 0)

print(max_value)
print(min_value)


