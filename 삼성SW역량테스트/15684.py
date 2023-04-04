import sys
input = sys.stdin.readline


N, M, H = map(int, input().split())
board = [[0]*N for _ in range(H)]
ans = 4
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1


def check():
    for i in range(N):
        tmp = i
        for j in range(H):
            if board[j][tmp]:
                tmp += 1
            elif tmp > 0 and board[j][tmp-1]:
                tmp -= 1
        if tmp != i:
            return False
    return True


def dfs(cnt, y, x):
    global ans
    if ans <= cnt:
        return
    if check():
        ans = min(ans, cnt)
    if cnt == 3:
        return
    for i in range(y, H):
        if i == y:
            k = x
        else:
            k = 0
        for j in range(k, N-1):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(cnt+1, i, j + 2)
                board[i][j] = 0

dfs(0, 0, 0)
if ans <= 3:
    print(ans)
else:
    print(-1)
