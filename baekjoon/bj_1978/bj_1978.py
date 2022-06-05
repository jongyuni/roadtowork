import sys
N = int(input())
num = list(map(int,sys.stdin.readline().split()))
cnt = 0

for n in num:
  flag = False
  if n == 1:
    continue
  elif n == 2:
    cnt += 1
    continue
  elif n % 2 == 0 :
    continue
  for x in range(2,n):
    if n % x != 0:
      continue
    else:
      flag = True
      break
  if not flag:
    cnt += 1

print(cnt)
