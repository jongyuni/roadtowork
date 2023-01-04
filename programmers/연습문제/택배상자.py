from collections import deque


def solution(order):
    answer = 0
    n = len(order)
    main_line = deque()

    for i in range(1, n + 1):
        main_line.append(i)

    sub_line = []
    i = 0

    while i < n:
        p = order[i]
        m = main_line[0] if main_line else 0
        s = sub_line[-1] if sub_line else 0

        if p == m:
            i += 1
            answer += 1
            main_line.popleft()
            continue
        elif p == s:
            i += 1
            answer += 1
            sub_line.pop()
            continue
        elif p > m:
            if m > 0:
                sub_line.append(main_line.popleft())
                continue
            break
        elif p < s:
            break

    return answer
