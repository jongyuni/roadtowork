import sys
N = int(input())
num = list(map(int, sys.stdin.readline().split()))
answer = [-1]*N
stack = []
count_dict = {}

for n in num:
  if n in count_dict.keys():
    count_dict[n] += 1
  else:
    count_dict[n] = 1

for i in range(N):
  while stack and count_dict[num[stack[-1]]] < count_dict[num[i]]:
    answer[stack.pop()] = num[i]
  stack.append(i)


for i in answer:
  print(i, end=" ")
