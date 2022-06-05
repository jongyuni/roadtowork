import sys
N = int(sys.stdin.readline())
case = [1, 3]

for _ in range(2,N+1):
  case[0], case[1] = case[1]%9901, (2*case[1]+case[0])%9901

print(case[-1])
