import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        one = heapq.heappop(scoville)

        if one >= K:
            break

        if not scoville:
            answer = -1
            break

        two = heapq.heappop(scoville)

        tmp = one + 2 * two
        heapq.heappush(scoville, tmp)
        answer += 1

    return answer
