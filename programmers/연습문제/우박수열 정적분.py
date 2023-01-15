def solution(k, ranges):
    answer = []
    nums = [k]
    area = [0]

    while k != 1:
        t = k
        if k % 2 == 1:
            k = 3 * k + 1
        else:
            k = k // 2
        nums.append(k)
        area.append((t + k) / 2 + area[-1])

    for rng in ranges:
        s_i, e_i = rng
        e_i += len(area) - 1
        if s_i == e_i:
            answer.append(0)
        elif s_i > e_i:
            answer.append(-1)
        else:
            answer.append(area[e_i] - area[s_i])

    return answer
