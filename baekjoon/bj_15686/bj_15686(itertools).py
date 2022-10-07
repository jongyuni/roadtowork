from itertools import combinations

N, M = map(int, input().split())
city = list()
city_chicken = 99999999
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

for comb in combinations(chicken, M):
    homes_chickens = 0
    for h in home:
        home_chicken = 99999
        for c in comb:
            home_chicken = min(home_chicken, abs(h[0]-c[0])+abs(h[1]-c[1]))
        homes_chickens += home_chicken
    city_chicken = min(city_chicken, homes_chickens)

print(city_chicken)
