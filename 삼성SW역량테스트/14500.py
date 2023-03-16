import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = list()
for _ in range(N):
    board.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]
ans = 0
dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
rotation = [[(1, 0), (0, -1), (0, 1)], # ㅗ
            [(-1, 0), (0, 1), (1, 0)], # ㅏ
            [(-1, 0), (0, -1), (1, 0)], # ㅓ
            [(0, -1), (0, 1), (1, 0)]] # ㅜ
def dfs(y, x, s, d):
    global ans
    if d == 4:
        ans = max(ans, s)
        return
    
    for i in range(4):
        ty = y + dy[i]
        tx = x + dx[i]
        if 0 <= ty < N and 0 <= tx < M and not visited[ty][tx]:
            visited[ty][tx] = True
            dfs(ty, tx, s+board[ty][tx], d+1)
            visited[ty][tx] = False

def another(y, x):
    global ans
    for i in range(4):
        tmp = board[y][x]
        for j in range(3):
            ty = y + rotation[i][j][0]
            tx = x + rotation[i][j][1]
            if not (0 <= ty < N and 0 <= tx < M):
                tmp = 0
                break
            tmp += board[ty][tx]
        ans = max(ans, tmp)
 
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        another(i, j)
print(ans)