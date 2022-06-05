import sys

N = int(sys.stdin.readline().rstrip())
test_cases = []

for _ in range(N):
  test_cases.append(int(sys.stdin.readline()))

m = max(test_cases)

prime = [True]*(m+1)
prime[0] = False
prime[1] = False

for i in range(2,int(m**0.5)+1):
  if prime[i]:
    for j in range(i*2,m+1,i):
      prime[j] = False


for case in test_cases:
  counter = 0
  for i in range((case//2)+1):
    if prime[i] and prime[case-i]:
      counter += 1
  print(counter)
