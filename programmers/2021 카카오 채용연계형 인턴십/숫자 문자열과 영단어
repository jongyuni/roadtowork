def solution(s):
    answer = ''
    alpha = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    num = "0123456789"
    tmp = ''
    for t in s:
        if t in num:
            answer += t
        else:
            tmp += t
            if tmp in alpha:
                answer += str(alpha.index(tmp))
                tmp = ''

    return int(answer)
