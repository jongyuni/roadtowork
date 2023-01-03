def isCorrect(number):
    for n in number:
        if n < 0:
            break
    else:
        if sum(number) == 0:
            return True
    return False


def solution(want, number, discount):
    answer = 0
    check = set(want)

    for i in range(10):
        if discount[i] in check:
            number[want.index(discount[i])] -= 1

    if isCorrect(number):
        answer += 1

    for i in range(10, len(discount)):
        if discount[i - 10] in check:
            number[want.index(discount[i - 10])] += 1
        if discount[i] in check:
            number[want.index(discount[i])] -= 1

        if isCorrect(number):
            answer += 1

    return answer
