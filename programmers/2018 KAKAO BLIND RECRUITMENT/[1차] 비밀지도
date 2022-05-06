def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = ''
        x = format(arr1[i],'b')
        y = format(arr2[i],'b')
        if len(x) > n:
            x = x[-n:]
        else:
            p = n - len(x)
            x = '0' * p + x
        if len(y) > n:
            y = y[-n:]
        else:
            p = n - len(y)
            y = '0' * p + y

        for j in range(n):
            if x[j] == '0' and y[j] == '0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
    return answer
