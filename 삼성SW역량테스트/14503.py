import sys
input = sys.stdin.readline

# 0은 청소 x, 1은 벽, 2는 청소 o
# 위는 0, 오른쪽 1, 아래는 2, 왼쪽 3
# 3, 0, 1, 2 -> 반시계 90도
# 2, 3. 0, 1
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)

N, M = map(int, input().split())
y, x, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def check(y, x):
    for dir in range(4):
        ty = y + dy[dir]
        tx = x + dx[dir]
        if board[ty][tx] == 1 or board[ty][tx] == 2:
            continue
        else:
            return True
    return False

def move():
    global y, x, d, ans
    if check(y, x):
        d = d-1 if d-1 >= 0 else 3
        if board[y+dy[d]][x+dx[d]] == 0:
            y = y + dy[d]
            x = x + dx[d]
            board[y][x] = 2
            ans += 1
    else:
        dd = 0
        if d == 0 or d == 2: dd = abs(d-2)
        else: dd = abs(d-4)
        if board[y+dy[dd]][x+dx[dd]] == 1:
            return False
        elif board[y+dy[dd]][x+dx[dd]] == 0:
            y = y + dy[dd]
            x = x + dx[dd]
            board[y][x] = 2
        else:
            y = y + dy[dd]
            x = x + dx[dd]
    return True

def pb():
    for i in range(N):
        for j in range(M):
            print(f'{board[i][j]} ', end='')
        print()
    print()

if board[y][x] == 0:
    board[y][x] = 2
    ans += 1

flag = True
while flag:
    flag = move()
print(ans)