import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
computer = list()
M = int(input())
start = list()
for m in range(M):
    a, b = map(int, input().split())
    computer.append((a, b))
    computer.append((b, a))
    if a == 1:
        start.append(b)
    elif b == 1:
        start.append(a)
visited = [False] * (N+1)
q = deque()
visited[1] = True
for s in start:
    visited[s] = True
    q.append(s)
while q:
    t = q.popleft()
    for a, b in computer:
        if a == t and not visited[b]:
            visited[b] = True
            q.append(b)
print(sum(visited)-1)