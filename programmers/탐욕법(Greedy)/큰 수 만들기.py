def solution(number, k):
    stack = []

    for n in number:
        if not stack or k == 0:
            stack.append(n)
            continue

        while k > 0 and stack:
            if int(n) <= int(stack[-1]):
                break
            elif int(n) > int(stack[-1]):
                stack.pop()
                k -= 1

        stack.append(n)

    answer = ''.join(stack[:len(stack)-k])

    return answer
