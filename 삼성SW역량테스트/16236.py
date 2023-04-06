import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
board = [[0] * N for _ in range(N)]
y, x = 0, 0
dy, dx = (0, 0, -1, 1), (1, -1, 0, 0)
level = 2
visited = [[False] * N for _ in range(N)]
for i in range(N):
    a = list(map(int, input().split()))
    for j, v in enumerate(a):
        if v == 9:
            y, x = i, j
        board[i][j] = v


def print_board():
    for i in range(N):
        for j in range(N):
            print(f'{board[i][j]} ', end='')
        print()
    print()


def bfs(y, x):
    q = deque()
    q.append((0, y, x))
    visited[y][x] = True
    fish = list()
    while q:
        d, a, b = q.popleft()
        for i in range(4):
            ty, tx = a+dy[i], b+dx[i]
            if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
                if board[ty][tx] < level and board[ty][tx] != 0:
                    fish.append((d+1, ty, tx))
                elif board[ty][tx] == level or board[ty][tx] == 0:
                    visited[ty][tx] = True
                    q.append((d+1, ty, tx))
                else:
                    continue
    if fish:
        return min(fish)
    return -1, -1, -1

cnt = 0
ans = 0
while True:
    d, a, b = bfs(y, x)
    if a < 0:
        break
    else:
        board[y][x] = 0
        board[a][b] = 9
        y, x = a, b
        cnt += 1
        if level == cnt:
            cnt = 0
            level += 1
        ans += d
    visited = [[False] * N for _ in range(N)]
print(ans)
