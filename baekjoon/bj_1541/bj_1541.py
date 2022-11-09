import sys

formula = sys.stdin.readline().strip().split('-')
answer = 0


def newSum(value):
    sum = 0
    temp = str(value).split('+')
    for t in temp:
        sum += int(t)
    return sum


for i in range(len(formula)):
    temp = newSum(formula[i])
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)
