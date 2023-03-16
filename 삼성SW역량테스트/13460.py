import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)

_map = [['.' for _ in range(M)] for _ in range(N)]
R = [0, 0]
B = [0, 0]
for i in range(N):
    a = list(input())
    for j in range(M):
        if a[j] == 'R':
            R[0], R[1] = i, j
            _map[i][j] = '.'
        elif a[j] == 'B':
            B[0], B[1] = i, j
            _map[i][j] = '.'
        elif a[j] == '#':
            _map[i][j] = a[j]
        elif a[j] == 'O':
            _map[i][j] = a[j]
            
def move(y, x, dy, dx):
    cnt = 0
    while _map[y+dy][x+dx] != '#' and _map[y][x] != 'O':
        y = y + dy
        x = x + dx
        cnt += 1
    return y, x, cnt
    
def bfs(ry, rx, by, bx, d):
    Q = deque()
    Q.append((ry, rx, by, bx, d))
    visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visited[ry][rx][by][bx] = True
    while Q:
        ry, rx, by, bx, d = Q.popleft()
        if d > 10:
            break
        for i in range(4):
            nry, nrx, rcnt = move(ry, rx, dy[i], dx[i])
            nby, nbx, bcnt = move(by, bx, dy[i], dx[i])
            if _map[nby][nbx] == 'O': continue
            if _map[nry][nrx] == 'O':
                print(d)
                return
            if nby == nry and nbx == nrx:
                if rcnt > bcnt:
                    nry -= dy[i]
                    nrx -= dx[i]
                else:
                    nby -= dy[i]
                    nbx -= dx[i]            
            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                Q.append((nry, nrx, nby, nbx, d+1))
    print(-1)

bfs(R[0], R[1], B[0], B[1], 1)