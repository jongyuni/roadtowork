import sys

n = int(sys.stdin.readline())
cases = list(map(int,sys.stdin.readline().split()))
d = [1] * n

for i in range(n):
  for j in range(i):
    if cases[i] > cases[j]:
      d[i] = max(d[i],d[j]+1)

m = max(d)  
print(m)
answer = []
d.reverse()

for i,v in enumerate(d):
  if v == m:
    answer.append(cases[len(d)-1-i])
    m -= 1

answer.reverse()

for i in answer:
  print(i, end=" ")
