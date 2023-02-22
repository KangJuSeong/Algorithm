import sys
from collections import deque
input = sys.stdin.readline


N, M, V = map(int, input().split())
E = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
Q = deque()

for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)
    
for i in range(N+1):
    E[i].sort()

def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in E[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    Q.append(start)
    visited[start] = True
    while Q:
        node = Q.popleft()
        print(node, end=' ')
        for i in E[node]:
            if not visited[i]:
                visited[i] = True
                Q.append(i)

dfs(V)
print()
visited = [False for _ in range(N+1)]
bfs(V)