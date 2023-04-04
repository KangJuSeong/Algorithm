import sys
input = sys.stdin.readline


N = int(input())
dy, dx = (0, -1, 0, 1), (1, 0, -1, 0)
visited = [[False]*101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    visited[x][y] = True

    move = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i-1] + 1) % 4)
        move.extend(tmp)

    for i in move:
        tx = x + dx[i]
        ty = y + dy[i]
        visited[tx][ty] = True
        x, y = tx, ty

ans = 0
for i in range(100):
    for j in range(100):
        if visited[i][j] and visited[i+1][j] and visited[i][j+1] and visited[i+1][j+1]:
            ans += 1
print(ans)
