def solution(n, a, b):
    answer = 0

    while True:
        answer += 1

        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1

        if a == b:
            break

        a = a // 2
        b = b // 2

    return answer
