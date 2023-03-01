import sys

input = sys.stdin.readline

n = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)
answer = drinks[0]

for i in range(1, n):
    answer += drinks[i] / 2

if str(answer).endswith('5'):
    print(answer)
else:
    print(int(answer))
