N, M = map(int, input().split())


def findK(number, K):
    count = 0
    while number >= K:
        count += number // K
        number = number // K
    return count


five_count = findK(N, 5) - findK(M, 5) - findK(N - M, 5)
two_count = findK(N, 2) - findK(M, 2) - findK(N - M, 2)

print(min(five_count, two_count))
