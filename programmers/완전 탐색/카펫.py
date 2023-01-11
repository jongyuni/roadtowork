def solution(brown, yellow):
    answer = []
    cases = [(yellow, 1)]

    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            cases.append((yellow // i, i))

    for g, s in cases:
        t = 2 * (g + s) + 4
        if t == brown:
            answer.append(g + 2)
            answer.append(s + 2)
            break

    return answer
