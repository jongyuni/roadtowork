from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people_que = deque(people)

    while len(people_que) > 1:
        m = people_que.pop()
        n = people_que.popleft()

        if m + n <= limit:
            answer += 1
            continue
        else:
            people_que.appendleft(n)
            answer += 1
            continue

    if people_que:
        answer += 1

    return answer
