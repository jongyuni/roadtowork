import sys
input = sys.stdin.readline

def func(k):
    if k == 0:
        return '-'
    return func(k-1) +  ' ' * (3 ** (k-1)) + func(k-1)

while True:
    try:
        N = int(input())
        print(func(N))
    except:
        break
