def dfs(now, remains, target, much):
    global answer
    if len(remains) == 1:
        if now + remains[0] == target:
            answer += 1
        if now - remains[0] == target:
            answer += 1
        return

    dfs(now + remains[0], remains[1:], target, much)
    dfs(now - remains[0], remains[1:], target, much)

    return


def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers[0], numbers[1:], target, 0)
    dfs(-numbers[0], numbers[1:], target, 0)
    return answer
