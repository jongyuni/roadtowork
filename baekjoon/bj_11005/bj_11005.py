import sys

N, B = map(int,sys.stdin.readline().rstrip().split())
R = ["0","1","2","3","4","5","6","7","8","9",
"A","B","C","D","E","F","G",
"H","I","J","K","L","M","N",
"O","P","Q","R","S","T","U",
"V","W","X","Y","Z"]
answer = ""

if N == 0:
  answer = "0"
else:
  while N != 0:
    answer = R[N%B] + answer
    N = N // B

print(answer) 
