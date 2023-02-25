import sys
from collections import deque
input = sys.stdin.readline


V = int(input())
A = [[] for _ in range(V+1)]
visited = [False] * (V+1)
distance = [0] * (V+1)
max_cost = 0

for i in range(V):
    E = list(map(int, input().split()))
    no = E.pop(0)
    E.pop(-1)
    while E:
        no2 = E.pop(0)
        cost = E.pop(0)
        A[no].append((no2, cost))

def bfs(node):
    visited[node] = True
    q = deque()
    q.append(node)
    while q:
        v = q.popleft()
        for i in A[v]:
            if not visited[i[0]]:    
                visited[i[0]] = True
                distance[i[0]] = distance[v] + i[1]
                q.append(i[0])
                    
bfs(1)
visited = [False for _ in range(V+1)]
mx = 1
for i in range(2, V+1):
    if distance[mx] < distance[i]:
        mx = i
distance = [0] * (V+1)
bfs(mx)
distance.sort()
print(distance[V])
