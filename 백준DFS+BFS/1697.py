import sys
input = sys.stdin.readline
from collections import deque


N, K = map(int, input().split())


def bfs():
    q = deque()
    q.append((N, 0))
    visited = [False for _ in range(100001)]
    while q:
        n, d = q.popleft()
        if n == K:
            return d
        if (0 <= n+1 <= 100000) and not visited[n+1]:
            q.append((n+1, d+1))
            visited[n+1] = True
        if (0 <= n-1 <= 100000) and not visited[n-1]:
            q.append((n-1, d+1))
            visited[n-1] = True
        if (0 <= 2*n <= 100000) and not visited[2*n]:
            q.append((2*n, d+1))
            visited[2*n]
print(bfs())
