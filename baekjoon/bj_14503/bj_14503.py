import sys
from collections import deque

def outofrange(y,x,N,M):
    return y < 0 or x < 0 or y >= N or x >= M

N, M = map(int, input().split())
R, C, D = map(int, input().split())
map_list = list()
cnt = 1

for _ in range(N):
    map_list.append(list(map(int,sys.stdin.readline().split())))

q = deque()
visited = [[False]*M for _ in range(N)]
plus = [(-1, 0), (0, 1), (1, 0), (0, -1)]
q.append((R, C, D))
visited[R][C] = True

# 북(0)의 왼쪽: 서(3) / 서(3)의 왼쪽: 남(2)/ 남(2)의 왼쪽: 동(1)/ 동(1)의 왼쪽: 북(0)
while q:
    sy, sx, sd = q.popleft()
    nd = (sd - 1) % 4
    ny = sy + plus[nd][0]
    nx = sx + plus[nd][1]
    if outofrange(ny, nx, N, M):
        continue
    # 왼쪽 청소가 안 되어 있는 경우, 벽이 아닌 경우
    if not visited[ny][nx] and not map_list[ny][nx]:
        visited[ny][nx] = True
        q.append((ny, nx, nd))
        cnt += 1
        continue
    # 왼쪽에 청소할 공간이 없는 경우
    if visited[ny][nx] or map_list[ny][nx]:
        # 네방향 청소가 되어 있거나 벽인 경우, 방향 그대로 후진
        for py, px in plus:
            if visited[sy + py][sx + px] or map_list[sy + py][sx + px]:
                continue
            else:
                q.append((sy, sx, nd))
                break
        else:
            ty = sy + plus[(sd - 2) % 4][0]
            tx = sx + plus[(sd - 2) % 4][1]
            if not map_list[ty][tx]:
                q.append((ty, tx, sd))
            else:  # 네방향 청소가 되어 있거나 벽이면서, 후진도 못 하는 경우 프로그램 종료
                q = deque()
        continue

print(cnt)
