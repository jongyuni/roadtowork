answer = 0


def dfs(k, dungeons, visited, count):
    global answer
    answer = max(answer, count)

    for j in range(len(dungeons)):
        if visited[j] or dungeons[j][0] > k:
            continue
        visited[j] = True
        dfs(k - dungeons[j][1], dungeons, visited, count + 1)
        visited[j] = False


def solution(k, dungeons):
    for i in range(len(dungeons)):
        cnt = 0
        visited = [False] * len(dungeons)
        visited[i] = True
        dfs(k - dungeons[i][1], dungeons, visited, cnt + 1)

    return answer
