import sys

N = int(sys.stdin.readline())
d=[[0]*10 for _ in range(N+1)]
d[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2,N+1):
  for j in range(10):
    if j == 0:
      d[i][j] = d[i-1][1]
    elif j == 9:
      d[i][j] = d[i-1][8]
    else:
      d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print(sum(d[N])%1000000000) 
