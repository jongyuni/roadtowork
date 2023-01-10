def solution(elements):
    answer = 0
    entire = set()
    tmp = elements * 2

    for e in elements:
        entire.add(e)

    for j in range(2, len(elements) + 1):
        for i in range(len(tmp) - j):
            entire.add(sum(tmp[i:i + j]))

    answer = len(entire)
    return answer
