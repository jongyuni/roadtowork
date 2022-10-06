def dfs(i, que):
    global city_chicken

    if len(que) == M:
        homes_chickens = 0
        for h in home:
            home_chicken = 99999999
            for q in que:
                home_chicken = min(home_chicken, abs(h[0] - q[0]) + abs(h[1] - q[1]))
            homes_chickens += home_chicken
        city_chicken = min(city_chicken, homes_chickens)
        return

    if i == len(chicken):
        return
    dfs(i+1, que + [chicken[i]])
    dfs(i+1, que)


N, M = map(int, input().split())
city = list()

for _ in range(N):
    city.append(list(map(int, input().split())))

home = list()
chicken = list()

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

city_chicken = 99999999
dfs(0, [])
print(city_chicken)
