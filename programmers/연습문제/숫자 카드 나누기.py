from math import gcd


def solution(arrayA, arrayB):
    answer = 0
    gcdA, gcdB = arrayA[0], arrayB[0]

    for i in range(1, len(arrayA)):
        gcdA = gcd(gcdA, arrayA[i])
        gcdB = gcd(gcdB, arrayB[i])
        
    for a in arrayA:
        if a % gcdB == 0:
            break
    else:
        answer = max(gcdB, answer)
    
    for b in arrayB:
        if b % gcdA == 0:
            break
    else:
        answer = max(gcdA, answer)
        
    return answer
