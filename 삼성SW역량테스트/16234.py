import sys
input = sys.stdin.readline
from collections import deque


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs(y, x):
    q = deque()
    temp = list()
    visited[y][x] = True
    q.append((y, x))
    temp.append((y, x))
    while q:
        _y, _x = q.popleft()
        for i in range(4):
            ty = _y + dy[i]
            tx = _x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
                if L <= abs(board[ty][tx] - board[_y][_x]) <= R:
                    visited[ty][tx] = True
                    q.append((ty, tx))
                    temp.append((ty, tx))
    return temp

ans = 0

while 1:
    visited = [[False] * (N+1) for _ in range(N+1)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                temp = bfs(i, j)
                if len(temp) > 1:
                    flag = 1
                    num = sum([board[n][m] for n, m in temp]) // len(temp)
                    for n, m in temp:
                        board[n][m] = num
    if flag:
        ans += 1
    else:
        break
print(ans)
    