import sys
N = int(sys.stdin.readline())
num = 1
for i in range(1,N+1):
  num *= i

ans = list(str(num))

for i in range(len(ans)):
  if int(ans[len(ans)-i-1]) > 0:
    print(i)
    break
