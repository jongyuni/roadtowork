import sys
import bisect

n = int(sys.stdin.readline())
cases = list(map(int,sys.stdin.readline().split()))
lists = [-1000000001]
d = []

for case in cases:
  if lists[-1] < case:
    lists.append(case)
    d.append((len(lists)-1,case))
  else:
    k = bisect.bisect_left(lists,case)
    lists[k] = case
    d.append((k,case))

m = len(lists)-1
print(m)
d.reverse()
answer = []

for t in d:
  if t[0] == m :
    answer.append(t[1])
    m -= 1
    continue

answer.reverse()

for a in answer:
  print(a, end=" ")
