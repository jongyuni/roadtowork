def solution(s):
    answer = []
    count = 0
    zero = 0

    while len(s) > 1:
        num = ""
        count += 1
        for n in s:
            if int(n) == 0:
                zero += 1
            else:
                num += n
        c = len(num)
        s = format(c, 'b')
        
    answer.append(count)
    answer.append(zero)

    return answer
