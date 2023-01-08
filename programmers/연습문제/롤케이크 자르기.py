from collections import Counter, defaultdict


def solution(topping):
    answer = 0
    one = Counter(topping)
    two = defaultdict(int)
    k = len(one)

    for top in topping:
        two[top] += 1
        one[top] -= 1

        if one[top] == 0:
            k -= 1

        if len(two) == k:
            answer += 1

    return answer
