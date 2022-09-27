def solution(msg):
    answer = []
    message = list(msg)
    dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    w = message.pop(0)
    c = ''

    while message:
        c = message[0]
        wc = w + c
        if wc not in dictionary:
            answer.append(dictionary.index(w) + 1)
            dictionary.append(wc)
            w = message.pop(0)
        else:
            message.pop(0)
            w = wc

    answer.append(dictionary.index(w)+1)
    return answer
