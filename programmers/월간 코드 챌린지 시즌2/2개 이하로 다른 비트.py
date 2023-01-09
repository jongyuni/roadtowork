def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue

        num = '0' + bin(number)[2:]
        i = num.rfind('0')
        new_num = list(num)
        new_num[i] = '1'
        new_num[i + 1] = '0'

        answer.append(int(''.join(new_num), 2))

    return answer
