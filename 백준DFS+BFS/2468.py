import sys
input = sys.stdin.readline
from collections import deque


dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
N = int(input())
board = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
limit = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    for j, v in enumerate(tmp):
        board[i][j] = v
        if v > limit:
            limit = v


def bfs(y, x, h):
    global visited
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    while q:
        _y, _x = q.popleft()
        for i in range(4):
            ty = _y + dy[i]
            tx = _x + dx[i]
            if 0<=ty<N and 0<=tx<N and not visited[ty][tx]:
                visited[ty][tx] = True
                if board[ty][tx] > h:
                    q.append((ty, tx))


ans = 0
for h in range(0, limit):
    area = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > h and not visited[i][j]:
                bfs(i, j, h)
                area +=1
    if ans < area:
        ans = area
    visited = [[False] * N for _ in range(N)]
print(ans)