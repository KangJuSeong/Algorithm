import sys
input = sys.stdin.readline
from collections import deque


F, S, G, U, D = map(int, input().split())
q = deque()
q.append((S, 0))
visited = [False for _ in range(F+1)]
visited[S] = True

def bfs():
    global q
    while q:
        floor, depth = q.popleft()
        if floor == G:
            return depth
        for i in (floor-D, floor+U):
            if 0 < i <= F and not visited[i]:
                visited[i] = True
                q.append((i, depth+1))
    return "use the stairs"


print(bfs())
