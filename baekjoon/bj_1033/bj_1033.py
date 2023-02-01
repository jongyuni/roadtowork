import sys, math

n = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
lcm_num = 1
value = [0] * n
visited = [False] * n

for _ in range(n - 1):
    a, b, p, q = map(int, sys.stdin.readline().split())
    graph[a].append([b, p, q])
    graph[b].append([a, q, p])
    lcm_num *= math.lcm(p, q)


def dfs(s):
    visited[s] = True

    for e, p, q in graph[s]:
        if visited[e]:
            continue
        value[e] = value[s] * q // p
        dfs(e)


value[0] = lcm_num
dfs(0)
gcd_num = value[0]

for i in range(1, n):
    gcd_num = math.gcd(gcd_num, value[i])

for v in value:
    print(int(v // gcd_num), end=' ')
