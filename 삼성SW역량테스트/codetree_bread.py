from collections import deque


dy, dx = (-1, 0, 0, 1), (0, -1, 1, 0)
# 1. 가장 가까운 베이스 캠프를 찾아서 시작 ( 같은 거리는 행이 작은 캠프부터) 1: basecamp
# 2. 해당 위치부터 움직이기 (움직일 때 경우의 수가 많으면 순서대로)
# 3. 도착한 베이스 캠프와 편의점은 해당 시간 이후부터는 지나다닐 수 없음
# 4. 모든 사람이 편의점 도착했을 때 시간


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
wait = deque()
user = [[0]*n for _ in range(n)]

for i in range(m):
    y, x = map(int, input().split())
    wait.append((y-1, x-1))


def user_board(y, x, k, py, px):
    global user
    user = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            user[i][j] = board[i][j]
    user[y][x] = 2
    user[y+dy[k]][x+dx[k]] = 3
    user[py][px] = 4
    for i in range(n):
        for j in range(n):
            print(f'{user[i][j]} ', end='')
        print()
    print()
            


def basecamp(y, x):  # 편의점 y, 편의점 x
    if board[y][x] == 1:
        return y, x
    q = deque()
    visited = [[False] * n for _ in range(n)]
    visited[y][x] = True
    q.append((y, x, 0))
    sub = list()
    while q:
        _y, _x, d = q.popleft()
        for i in range(4):
            ty = _y + dy[i]
            tx = _x + dx[i]
            if 0 <= ty < n and 0 <= tx < n and not visited[ty][tx] and board[ty][tx] != -1:
                if board[ty][tx] == 1:
                    visited[ty][tx] = True
                    sub.append((d+1, ty, tx))
                else:
                    visited[ty][tx] = True
                    q.append((ty, tx, d+1))
    result = sorted(sub)
    return result[0][1], result[0][2]


def move(y, x, py, px):
    q = deque()
    result = list()
    visited = [[False] * n for _ in range(n)]
    visited[py][px] = True
    q.append((py, px, 0))
    while q:
        gy, gx, d = q.popleft()
        for i in range(4):
            ty = gy + dy[i]
            tx = gx + dx[i]
            if 0 <= ty < n and 0 <= tx < n and not visited[ty][tx]:
                if y == ty and x == tx and (board[ty][tx] == -1 or board[ty][tx] == 0):
                    result.append((gy, gx, d+1))
                    visited[ty][tx] = True
                elif board[ty][tx] != -1:
                    q.append((ty, tx, d+1))
                    visited[ty][tx] = True
    result = sorted(result, key=lambda x:x[2])
    for r, c, d in result:
        for i in range(4):
            if y+dy[i] == r and x+dx[i] == c:
                return i
    return -1


time = 0
cnt = len(wait)
client = deque()


while cnt > 0:
    time += 1
    size = len(client)
    while size > 0:
        y, x, py, px = client.popleft()
        arrow = move(y, x, py, px)
        ty = y + dy[arrow]
        tx = x + dx[arrow]
        if ty == py and tx == px:
            cnt -= 1
            board[ty][tx] = -1
        else:
            client.append((ty, tx, py, px))
        size -= 1
    if wait:
        py, px = wait.popleft()
        y, x = basecamp(py, px)
        client.append((y, x, py, px))
        board[y][x] = -1
print(time)
