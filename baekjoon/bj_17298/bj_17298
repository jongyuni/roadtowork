import sys
N = int(input())
num = list(map(int, sys.stdin.readline().split()))
answer = [-1]*N
stack = []

for i in range(N):
  while stack and num[stack[-1]] < num[i]:
    answer[stack.pop()] = num[i]
  stack.append(i) 


for i in answer:
  print(i, end=" ")
