import sys

N, B = sys.stdin.readline().split()
R = ["0","1","2","3","4","5","6","7","8","9",
"A","B","C","D","E","F","G",
"H","I","J","K","L","M","N",
"O","P","Q","R","S","T","U",
"V","W","X","Y","Z"]
answer = 0

if N == 0:
  answer = 0
else:
  for i,n in enumerate(N):
    t = R.index(n) * int(B)**(len(N)-1-i) 
    answer += t  


print(answer) 
