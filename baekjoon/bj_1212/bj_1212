import sys

N = sys.stdin.readline().rstrip()
answer = ""
number = ["000","001","010","011","100","101","110","111"]

if N == "0":
  answer = "0"

else:
  for i in N:
    answer += number[int(i)]

  while answer[0] == "0":
    answer = answer[1:]

print(answer)
