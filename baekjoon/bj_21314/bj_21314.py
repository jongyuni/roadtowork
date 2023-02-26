import sys

input = sys.stdin.readline


def find(number):
    max_answer = ''
    min_answer = ''
    n = 0
    for num in number:
        if num == 'M':
            n += 1
            continue
        else:
            if n > 0:
                max_answer += str(5 * (10 ** n))
                min_answer += str(10 ** n + 5)
                n = 0
            else:
                max_answer += '5'
                min_answer += '5'
                n = 0

    if n > 0:
        max_answer += '1' * n
        min_answer += str(10 ** (n - 1))
    print(max_answer)
    print(min_answer)


mknum = input()

find(mknum.rstrip())
