import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
virus = list()
ans = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append((i, j))

def print_board(_board):
    for i in range(N):
        for j in range(M):
            print(f'{_board[i][j]} ', end='')
        print()
    print()

def wall(start, cnt):
    global ans
    if cnt == 3:
        _board = deepcopy(board)
        for v in virus:
            dfs(v[0], v[1], _board)
        tmp = 0
        for i in range(N):
            for j in range(M):
                if _board[i][j] == 0:
                    tmp += 1
        ans = max(ans, tmp)
        return
    else:
        for i in range(start, N*M): # 2차원 배열에서 조합 구하기
            r = i // M # 0 // 6, 
            c = i % M # 0 % 6, 
            print(r, c)
            if board[r][c] == 0 : # 안전영역인 경우 벽으로 선택가능
                board[r][c] = 1 # 벽으로 변경
                wall(i,cnt+1) # 벽선택
                board[r][c] = 0

def dfs(y, x, _board):
    for dir in range(4):
        ty = y + dy[dir]
        tx = x + dx[dir]
        if 0 <= ty < N and 0 <= tx < M:
            if _board[ty][tx] == 0:
                _board[ty][tx] = 2
                dfs(ty, tx, _board)

def bfs():
    global ans
    q = deque()
    for v in virus:
        q.append(v)
    _board = deepcopy(board)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if 0 <= ty < N and 0 <= tx < M:
                _board[ty][tx] = 2
                q.append((ty, tx))
    tmp = 0
    for i in range(N):
        for j in range(M):
            if _board[i][j] == 0:
                tmp += 1
    del _board
    ans = max(ans, tmp)
    print(ans)

wall(0, 0)
print(ans)
