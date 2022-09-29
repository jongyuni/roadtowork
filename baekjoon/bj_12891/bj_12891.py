import sys

S, P = map(int, sys.stdin.readline().split())
DNA = sys.stdin.readline().strip()
a, c, g, t = map(int, sys.stdin.readline().split())
answer = 0
check = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
tmp = DNA[:P]

for m in tmp:
    check[m] += 1

if check['A'] >= a and check['C'] >= c and check['G'] >= g and check['T'] >= t:
    answer += 1
s = 0
e = P
for i in range(S-P):
    check[DNA[s+i]] -=1
    check[DNA[e+i]] += 1
    if check['A'] >= a and check['C'] >= c and check['G'] >= g and check['T'] >= t:
        answer += 1

print(answer)
