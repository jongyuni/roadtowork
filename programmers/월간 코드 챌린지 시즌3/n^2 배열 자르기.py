def solution(n, left, right):
    answer = []
    s_i, s_j = divmod(left, n)
    e_i, e_j = divmod(right, n)

    for i in range(s_i, e_i + 1):
        m = 0
        if i == s_i:
            m = s_j
        if i == e_i:
            n = e_j + 1
        for j in range(m, n):
            answer.append(max(i + 1, j + 1))

    return answer
