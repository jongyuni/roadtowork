def solution(id_list, report, k):
    answer = []
    table = [[ 0 ] * len(id_list) for _ in range(len(id_list))]

    for rep in report:
        tmp = rep.split()
        i = id_list.index(tmp[0])
        j = id_list.index(tmp[1])

        if table[i][j] == 0:
            table[i][j] += 1
        else:
            continue

    most_reported = []

    for i in range(len(id_list)):
        t = 0
        for j in range(len(id_list)):
            t += table[j][i]
        if t >= k:
            most_reported.append(i)

    for i in range(len(id_list)):
        a = 0
        for j in most_reported:
            a += table[i][j]
        answer.append(a)

    return answer
