import sys
N = int(sys.stdin.readline())
case = []

for _ in range(N):
  cost = list(map(int,sys.stdin.readline().split()))
  case.append(cost)

for i in range(1,N):
  case[i][0] += min(case[i-1][1],case[i-1][2])
  case[i][1] += min(case[i-1][0],case[i-1][2])
  case[i][2] += min(case[i-1][0],case[i-1][1])

print(min(case[-1]))
