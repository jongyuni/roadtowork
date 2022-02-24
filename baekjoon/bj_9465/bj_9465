import sys
T = int(sys.stdin.readline())
answer = []
for _ in range(T):
  n = int(sys.stdin.readline())
  total = [[0]*3 for i in range(n)]
  costs = []
  cost1 = list(map(int,sys.stdin.readline().split()))
  costs.append(cost1)
  cost2 = list(map(int,sys.stdin.readline().split()))
  costs.append(cost2)
  total[0] = [cost1[0],cost2[0],0]
  
  for i in range(1,n):
    total[i][0] = max(total[i-1][1],total[i-1][2]) + cost1[i]
    total[i][1] = max(total[i-1][0],total[i-1][2]) + cost2[i]
    total[i][2] = max(total[i-1][0],total[i-1][1])

  answer.append(max(total[-1]))

for a in answer:
  print(a)
