def solution(cards):
    answer = 0
    visited = [False] * (len(cards) + 1)
    one = 0
    two = 0

    for card in cards:
        if visited[card]:
            continue

        cnt = 0
        stack = list()
        stack.append(card)

        while stack:
            c = stack.pop()
            if visited[c]:
                break
            visited[c] = True
            cnt += 1
            stack.append(cards[c - 1])

        if cnt > one:
            one, two = cnt, one
            continue
        elif cnt > two:
            two = cnt
            continue

    answer = one * two
    return answer
