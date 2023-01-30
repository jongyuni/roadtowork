import sys


def isPalindrome(num):
    tmp = list(str(num))
    i = 0
    j = len(tmp) - 1
    while i < j:
        if tmp[i] != tmp[j]:
            return False
        i += 1
        j -= 1

    return True


n = int(sys.stdin.readline())
answer = 0
num = [0] * 10000001

for i in range(2, 10000001):
    num[i] = i

for i in range(2, int(10000001 ** 0.5) + 1):
    if num[i] == 0:
        continue
    for j in range(i + i, 10000001, i):
        num[j] = 0

for i in range(n, 10000001):
    if num[i] == 0:
        continue
    answer = num[i]
    if isPalindrome(answer):
        print(answer)
        break
