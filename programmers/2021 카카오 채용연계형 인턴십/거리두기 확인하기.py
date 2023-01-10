def getresult(place):
    p_locs = []

    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                p_locs.append([i, j])
                
    for i in range(len(p_locs)):
        c = p_locs[i]

        for j in range(i + 1, len(p_locs)):
            n = p_locs[j]
            d = abs(c[0] - n[0]) + abs(c[1] - n[1])

            if d > 2:
                continue
            elif d == 1:
                return 0
            elif d == 2:
                if c[0] == n[0] and place[c[0]][c[1] + 1] == 'O':
                    return 0
                elif c[1] == n[1] and place[c[0] + 1][c[1]] == 'O':
                    return 0
                elif place[c[0]][n[1]] == 'O' or place[n[0]][c[1]] == 'O':
                    return 0

            

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(getresult(place))

    return answer
