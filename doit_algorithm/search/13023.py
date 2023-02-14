import sys
input = sys.stdin.readline


N, M = map(int, input().split())
E = [[] for _ in range(N)]
visited = [False for _ in range(N)]
flag = False

for _ in range(M):
    a, b = map(int, input().split())
    E[a].append(b)
    E[b].append(a)

def dfs(v, depth):
    global flag
    if depth == 5:
        flag = True
        return
    visited[v] = True
    for i in E[v]:
        if not visited[i]:
            dfs(i, depth+1)
    visited[v] = False

for i in range(N):
    dfs(i, 1)
    if flag:
        break

if flag: print(1)
else: print(0)
    