import sys

input = sys.stdin.readline

n = int(input())
honey = list(map(int, input().split()))
answer = 0

hoeny_sum = []
hoeny_sum.append(honey[0])

for i in range(1, n):
    hoeny_sum.append(hoeny_sum[i - 1] + honey[i])

for i in range(1, n - 1):
    answer = max(answer, 2 * hoeny_sum[n - 1] - honey[0] - honey[i] - hoeny_sum[i])

for i in range(1, n - 1):
    answer = max(answer, hoeny_sum[n - 2] - honey[i] + hoeny_sum[i - 1])

for i in range(1, n - 1):
    answer = max(answer, hoeny_sum[n - 2] - honey[0] + honey[i])
    
print(answer)
