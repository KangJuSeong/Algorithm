import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
start, end = map(int, input().split())
edge = list()
M = int(input())
q = deque()
visited = [False] * (N+1)
for m in range(M):
    a, b = map(int, input().split())
    edge.append((a, b))
    edge.append((b, a))
    if a == start:
        visited[a] = True
        visited[b] = True
        q.append((b, 1))
    elif b == start:
        visited[a] = True
        visited[b] = True
        q.append((a, 1))


def bfs():
    global q, visited
    while q:
        v, d = q.popleft()
        for v1, v2 in edge:
            if v == v1 and not visited[v2]:
                if v2 == end:
                    return d+1
                else:
                    visited[v2] = True
                    q.append((v2, d+1))
    return -1
print(bfs())
