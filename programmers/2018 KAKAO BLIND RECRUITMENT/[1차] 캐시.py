def solution(cacheSize, cities):
    answer = 0
    cache = []

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        city = city.lower()
        if city not in cache:
            answer += 5
            cache.append(city)
            if len(cache) >= cacheSize:
                cache.pop(0)
        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)

    return answer
