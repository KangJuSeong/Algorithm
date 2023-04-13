import sys
input = sys.stdin.readline
from collections import deque


dy, dx = (0, 0, 1, -1), (1, -1, 0, 0)
N = int(input())
board = list()
for n in range(N):
    a = input()
    a = list(map(int, a[:-1]))
    board.append(a)
visited = [[False] * N for _ in range(N)]

def bfs(y, x):
    global visited
    q = deque()
    visited[y][x] = True
    q.append((y, x))
    result = 1
    while q:
        _y, _x = q.popleft()
        for i in range(4):
            ty = _y + dy[i]
            tx = _x + dx[i]
            if (0 <= ty < N and 0 <= tx < N) and not visited[ty][tx] and board[ty][tx] == 1:
                visited[ty][tx] = True
                q.append((ty, tx))
                result += 1
    return result

level = 0
ans = list()
for i in range(N):
    for j in range(N):
        if not visited[i][j] and board[i][j] == 1:
            result = bfs(i, j)
            ans.append(result)
            level += 1
print(level)
ans = sorted(ans)
for a in ans:
    print(a)
