changes = [500, 100, 50, 10, 5, 1]
N = int(input())
yen = 1000 - N
answer = 0

for c in changes:
    if yen // c > 0:
        answer += yen // c
        yen = yen % c
    else:
        continue

print(answer)
