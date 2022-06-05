N, K = map(int,input().split())
queue = [i for i in range(1, N+1)]
answer = []
num = K - 1

for _ in range(N):
  if len(queue) > num:
    answer.append(queue.pop(num))
    num += K-1
  else:
    num = num % len(queue)
    answer.append(queue.pop(num))
    num += K-1



print("<", ', '.join(str(i) for i in answer), ">", sep = '')
