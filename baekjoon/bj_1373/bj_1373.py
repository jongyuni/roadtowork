import sys

N = sys.stdin.readline().rstrip()
answer = ""

while len(N) % 3 != 0:
  N = "0" + N


for i in range(0,len(N),3):
  tmp = 4*int(N[-i-3]) + 2*int(N[-i-2]) + int(N[-i-1])
  answer = str(tmp) + answer

print(answer)
