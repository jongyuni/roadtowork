import sys
import math
sys.setrecursionlimit(10 ** 6)

def convert(num,base):
    tmp = "0123456789"
    q,r = divmod(num,base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q,base) + tmp[r]

def isPrime(num):
    root = math.sqrt(num)
    for i in range(2,int(root)+1):
        if num%i == 0: #나눠지면
            return 0
    return 1

def solution(n, k):
    answer = 0
    knum = convert(n,k)
    cnum = knum.split("0")
    
    for i in range(len(cnum)):
        tmp = cnum[i]
        if not tmp:
            continue
        if int(tmp) > 1:
            answer += isPrime(int(tmp))
        
    return answer
