def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    group = []

    for i in range(row_begin - 1, row_end):
        now = data[i]
        tmp = 0
        for n in now:
            tmp += n % (i + 1)
        group.append(tmp)

    for now in group:
        answer = answer ^ now

    return answer
