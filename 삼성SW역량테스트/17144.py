import sys
input = sys.stdin.readline


R, C, T = map(int, input().split())
board = [[0] * C for _ in range(R)]
ay, by = -1, -1
dy, dx = (0, 0, -1, 1), (-1, 1, 0, 0)
for r in range(R):
    c = list(map(int, input().split()))
    for i, v in enumerate(c):
        if v == -1 and ay < 0:
            ay = r
        elif v == -1 and ay >= 0:
            by = r
        board[r][i] = v


def print_board():
    for i in range(R):
        for j in range(C):
            print(f'{board[i][j]} ', end='')
        print()
    print()


def spread():
    tmp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0 or board[r][c] == -1:
                continue
            mount = board[r][c] // 5
            for arrow in range(4):
                ty = r + dy[arrow]
                tx = c + dx[arrow]
                if 0 <= ty < R and 0 <= tx < C and board[ty][tx] != -1:
                    tmp[ty][tx] += mount
                    board[r][c] -= mount
    for r in range(R):
        for c in range(C):
            board[r][c] += tmp[r][c]


def air(y, arrow):
    if arrow == 0:
        new_arr = [[0] * C for _ in range(y)]
        for i in range(y):
            for j in range(C):
                if j == 0 and i == y-1:
                    new_arr[i][j+1] = 0
                elif j == 0 and i == y-2:
                    new_arr[i+1][j] = -1
                elif j == 0 and i < y-2:
                    new_arr[i+1][j] = board[i][j]
                elif j == (C-1) and i > 0:
                    new_arr[i-1][j] = board[i][j]
                elif 0 < j <= (C-1) and i == 0:
                    new_arr[i][j-1] = board[i][j]
                elif 0 < j <= (C-1) and i == (y-1):
                    new_arr[i][j+1] = board[i][j]
                else:
                    new_arr[i][j] = board[i][j]
        for i in range(y):
            for j in range(C):
                board[i][j] = new_arr[i][j]
    else:
        new_arr = [[0] * C for _ in range(R-y+1)]
        for i in range(R-y+1):
            for j in range(C):
                if j == 0 and i == 0:
                    new_arr[i][j+1] = 0
                elif i == 0 and 0 < j < C-1:
                    new_arr[i][j+1] = board[y-1][j]
                elif 0 <= i < R-y and j == C-1:
                    new_arr[i+1][j] = board[i+y-1][j]
                elif i == R-y and 0 < j <= C-1:
                    new_arr[i][j-1] = board[R-1][j]
                elif j == 0 and i == 1:
                    new_arr[0][0] = -1
                elif j == 0 and 1 < i <= R-y:
                    new_arr[i-1][j] = board[i+y-1][j]
                else:
                    new_arr[i][j] = board[i+y-1][j]
        for i in range(R-y+1):
            for j in range(C):
                board[i+y-1][j] = new_arr[i][j]


def total():
    ans = 0
    for r in range(R):
        ans += sum(board[r])
    ans += 2
    return ans

for i in range(T):
    spread()
    air(ay+1, 0)
    air(by+1, 1)
print(total())