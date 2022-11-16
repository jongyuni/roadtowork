import sys

input = sys.stdin.readline
N, M = map(int, input().split())
min_six = int(sys.maxsize)
min_each = int(sys.maxsize)

for _ in range(M):
    d, e = map(int, input().split())
    min_six = min(min_six, d)
    min_each = min(min_each, e)
    
answer = N * min_each
n_six = N // 6 + 1
answer = min((n_six * min_six), answer)
n_six -= 1

base_cost = n_six * min_six
temp = (N - n_six * 6) * min_each
cost = base_cost + temp

answer = min(answer, cost)

print(answer)
