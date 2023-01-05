def solution(k, d):
    answer = 0

    for a in range(0, d + 1, k):
        t = (d ** 2 - a ** 2) ** (1 / 2)
        s = round(t // k) + 1
        answer += s

    return answer
