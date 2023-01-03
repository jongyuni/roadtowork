from collections import defaultdict


def solution(k, tangerine):
    answer = 0
    many = defaultdict(int)
    now = 0

    for t in tangerine:
        many[t] += 1

    guls = list(zip(many.values(), many.keys()))
    guls.sort(reverse=True)

    for gul in guls:
        now += gul[0]
        answer += 1
        if now >= k:
            break

    return answer
