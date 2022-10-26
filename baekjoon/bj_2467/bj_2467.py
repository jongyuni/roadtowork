import sys

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
i, j = 0, len(nums) - 1
level = 2000000000
answer = []

while i <= j:
    cur = nums[i] + nums[j]
    if i == j:
        break
    if abs(cur) <= level:
        level = abs(cur)
        answer = [nums[i], nums[j]]
    if cur < 0:
        i += 1
    elif cur > 0:
        j -= 1
    else:
        answer = [nums[i], nums[j]]
        break

for a in answer:
    print(a, end=' ')
