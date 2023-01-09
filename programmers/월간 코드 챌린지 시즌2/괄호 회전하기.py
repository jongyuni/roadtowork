def solution(s):
    answer = 0

    for i in range(len(s)):
        tmp = list(s)[i:] + list(s)[:i]
        stack = list()
        flag = False

        for t in tmp:
            if t == '[' or t == '{' or t == '(':
                stack.append(t)
                continue

            if not stack:
                flag = False
                break

            p = stack.pop()

            if t == ']' and p == '[':
                flag = True
                continue
            elif t == '}' and p == '{':
                flag = True
                continue
            elif t == ')' and p == '(':
                flag = True
                continue
            else:
                flag = False
                stack.append(t)

        if not stack and flag:
            answer += 1

    return answer
