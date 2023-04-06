import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque

# 1 = 벽, 2 = 바이러스, 0 = 빈칸

ans = 50 * 50 + 1
N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]
virus = list()
dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
for y in range(N):
    a = list(map(int, input().split()))
    for x, v in enumerate(a):
        if v == 2:
            virus.append((y, x))
            board[y][x] = -1
        elif v == 1:
            board[y][x] = -2
        else:
            board[y][x] = 0

def print_board(map):
    for i in range(N):
        for j in range(N):
            print(f'{map[i][j]} ', end='')
        print()
    print()


def bfs(v, lab, visited):
    q = deque()
    for y, x in v:
        q.append((y, x, 0))
        lab[y][x] = -3
        visited[y][x] = True
    sec = 0
    while q:
        y, x, d = q.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and lab[ty][tx] == -1 and not visited[ty][tx]:
                visited[ty][tx] = True
                q.append((ty, tx, d+1))
                continue
            if 0 <= ty < N and 0 <= tx < N and lab[ty][tx] != -2 and not visited[ty][tx]:
                visited[ty][tx] = True
                lab[ty][tx] = d+1
                q.append((ty, tx, d+1))
                sec = d+1
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                return 50 * 50 + 1
    return sec


def dfs(q, d):
    global ans
    if len(q) == M:
        visited = [[False] * N for _ in range(N)]
        ans = min(ans, bfs(q, deepcopy(board), visited))
        return
    if d == len(virus):
        return
    q.append(virus[d])
    dfs(q, d+1)
    q.pop()
    dfs(q, d+1)
dfs(deque(), 0)

if ans == 50*50+1:
    print(-1)
else:
    print(ans)

