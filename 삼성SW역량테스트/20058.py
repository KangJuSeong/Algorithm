import sys
input = sys.stdin.readline
from collections import deque


dy, dx = (-1, 1, 0, 0), (0, 0, -1, 1)
N, Q = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))


def printing(map, n, m):
    for i in range(n):
        for j in range(m):
            print(f'{map[i][j]} ', end='')
        print()
    print()


def rotate(l):
    for row in range(0, 2**N, 2**l):
        for col in range(0, 2**N, 2**l):
            s = 2**l
            tmp = [[0] * s for _ in range(s)]
            for r in range(s):
                for c in range(s):
                    tmp[c][s-r-1] = ice[row+r][col+c]
            for r in range(s):
                for c in range(s):
                    ice[row+r][col+c] = tmp[r][c]


def melt():
    global ice
    tmp = [[0] * (2**N) for _ in range(2**N)]
    for r in range(2**N):
        for c in range(2**N):
            if ice[r][c] == 0:
                continue
            life = 0
            for i in range(4):
                ty = r+dy[i]
                tx = c+dx[i]
                if 0 <= ty < 2**N and 0 <= tx < 2**N:
                    if ice[ty][tx] > 0:
                        life += 1
            if life < 3:
                tmp[r][c] = ice[r][c] - 1
            else:
                tmp[r][c] = ice[r][c]
    ice = tmp


def lump(y, x):
    global visited
    q = deque()
    visited[y][x] = True
    q.append((y, x))
    size = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            ty = r + dy[i]
            tx = c + dx[i]
            if 0 <= ty < 2**N and 0 <= tx < 2**N and not visited[ty][tx] and ice[ty][tx] != 0:
                visited[ty][tx] = True
                q.append((ty, tx))
                size += 1
    return size



result = 0
for l in L:
    rotate(l)
    melt()


visited = [[False] * (2**N) for _ in range(2**N)]
ans = 0
for i in range(2**N):
    for j in range(2**N):
        ans += ice[i][j]
        if ice[i][j] != 0 and not visited[i][j]:
            a = lump(i, j)
            if a:
                result = max(result, a+1)
print(ans)
print(result)

