import sys

input = sys.stdin.readline

a = int(input())
t = int(input())
o = int(input())
bbun = 1
daegi = 1
game = []
n = 0
prev_t = 0

while True:
    prev_t = bbun
    n += 1
    for _ in range(2):
        game.append((bbun, 0))
        bbun += 1
        game.append((daegi, 1))
        daegi += 1

    for _ in range(n + 1):
        game.append((bbun, 0))
        bbun += 1

    for _ in range(n + 1):
        game.append((daegi, 1))
        daegi += 1
    
    if prev_t < t <= bbun:
        print(game.index((t, o)) % a)
        break
