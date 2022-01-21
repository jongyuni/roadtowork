import sys

N = int(input())
stack = []

for _ in range(N):
  lista = sys.stdin.readline().split()

  if lista[0] == "push":
    if lista[1]:
      stack.append(lista[1])

  elif lista[0] == "pop":
    if stack:
      print(stack.pop())
    else:
      print(-1)

  elif lista[0] == "size":
    print(len(stack))

  elif lista[0] == "empty":
    if not stack:
      print(1)
    else:
      print(0)

  elif lista[0] == "top":
    if not stack:
      print(-1)
    else:
      print(stack[-1])
