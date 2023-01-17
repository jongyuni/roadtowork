def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        if num == 1:
            answer.append(0)
            continue

        for i in range(2, int(num ** 0.5) + 1):
            j = num // i

            if j > 10 ** 7:
                continue

            if num % i == 0:
                answer.append(j)
                break
        else:
            answer.append(1)

    return answer
