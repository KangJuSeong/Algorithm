import sys
input = sys.stdin.readline
from collections import deque


dy, dx, dh = (0, 0, 1, -1, 0, 0), (1, -1, 0, 0, 0, 0), (0, 0, 0, 0, 1, -1)
M, N, H = map(int, input().split())
board = [[[0] * M for _ in range(N)] for _ in range(H)]
depth = [[[0] * M for _ in range(N)] for _ in range(H)]
# 익은 것 1, 안익은 것 0, 없는 것 -1
q = deque()
for h in range(H):
    for n in range(N):
        tmp = list(map(int, input().split()))
        for m, v in enumerate(tmp):
            board[h][n][m] = v
            if v == 1:
                q.append((h, n, m))  # h, n, m, d(일수)


def check():
    _max = -1
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if board[h][n][m] == 0:
                    return -1
                _max = max(_max, depth[h][n][m])
    return _max



def bfs(q):
    visited = [[[False] * M for _ in range(N)] for _ in range(H)]
    for h, n, m in q:
        visited[h][n][m] = True
    while q:
        h, n, m = q.popleft()
        for i in range(6):
            ty = n + dy[i]
            tx = m + dx[i]
            th = h + dh[i]
            if (0 <= ty < N and 0 <= tx < M and 0 <= th < H) and not visited[th][ty][tx] and board[th][ty][tx] == 0:
                depth[th][ty][tx] = depth[h][n][m] + 1
                board[th][ty][tx] = 1
                visited[th][ty][tx] = True
                q.append((th, ty, tx))

bfs(q)
print(check())
