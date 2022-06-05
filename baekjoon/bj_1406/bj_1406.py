import sys

left = list(sys.stdin.readline().strip())
N = int(input())
right = list()

for _ in range(N):
  order = sys.stdin.readline().split()

  if order[0] == 'L' and left:
    right.append(left.pop())
    
  elif order[0] == 'D' and right:
    left.append(right.pop())
    
  elif order[0] == 'B' and left:
    left.pop()

  elif order[0] == 'P':
    left.append(order[1])

print(''.join(left)+''.join(list(reversed(right))))
