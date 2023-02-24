import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[0]*M for _ in range(N)]
for i in range(N):
    line = list(input())
    for j in range(M):
        A[i][j] = int(line[j])

visited = [[False for _ in range(M)] for _ in range(N)]
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        now = q.popleft()
        for i in move:
            n = now[0] + i[0]
            m = now[1] + i[1]
            if n >= 0 and m >=0 and n < N and m < M:
                if A[n][m] != 0 and not visited[n][m]:
                    visited[n][m] = True
                    A[n][m] = A[now[0]][now[1]] + 1
                    q.append((n, m))
        
bfs(0, 0)
print(A[N-1][M-1])