def solution(s):
    result = []
    if len(s) == 1:
        return 1

    for i in range(1,(len(s)//2)+1):
        tmp = s[:i]
        b = ''
        cnt = 1

        for j in range(i, len(s), i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt == 1:
                    b += tmp
                else:
                    b += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1
        if cnt > 1:
            b += str(cnt) + tmp
        else:
            b += tmp
        result.append(len(b))

    return min(result)
