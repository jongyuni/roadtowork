from itertools import permutations


def isPrime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True


def solution(numbers):
    check = set()
    for i in range(1, len(numbers) + 1):
        for perm in permutations(list(numbers), i):
            tmp = ''
            for p in perm:
                tmp += p
            num = int(tmp)
            if num == 0 or num == 1:
                continue
            if isPrime(num):
                check.add(num)

    return len(check)
