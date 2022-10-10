from collections import deque

T = int(input())
plus = [(1,0), (0,-1), (-1,0), (0,1)]
answers = []
for _ in range(T):
    answer = 0
    M, N, K = map(int, input().split())
    farm = deque()
    visited = set()
    for _ in range(K):
        X, Y = map(int, input().split())
        farm.append((Y, X))

    while farm:
        tmp = deque()
        now_i, now_j = farm.popleft()
        tmp.append((now_i, now_j))
        before_length = len(visited)
        if (now_i, now_j) in visited:
            continue
        while tmp:
            now_i, now_j = tmp.popleft()
            if (now_i, now_j) in visited:
                continue
            visited.add((now_i, now_j))
            for plus_i, plus_j in plus:
                next_i = now_i + plus_i
                next_j = now_j + plus_j
                if next_i < 0 or next_i >= N or next_j < 0 or next_j >= M:
                    continue
                if (next_i, next_j) in visited:
                    continue
                if (next_i, next_j) in farm:
                    tmp.append((next_i, next_j))
        if before_length != len(visited):
            answer += 1

    answers.append(answer)

for a in answers:
    print(a)


