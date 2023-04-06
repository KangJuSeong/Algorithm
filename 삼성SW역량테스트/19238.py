import sys
input = sys.stdin.readline
from collections import deque


dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
r = r - 1
c = c - 1
client = list()
client_board = [[-1 for _ in range(N)] for _ in range(N)]
for m in range(M):
    y, x, i, j = map(int, input().split())
    client.append((y-1, x-1, i-1, j-1))
    client_board[y-1][x-1] = m


def taking_client(y, x):
    if client_board[y][x] != -1:
        return (0, client_board[y][x])
    visited = [[False for _ in range(N)] for _ in range(N)]
    take = 0
    q = deque()
    q.append((y, x, 0))
    visited[y][x] = True
    while q:
        _y, _x, d = q.popleft()
        for i in range(4):
            ty = _y + dy[i]
            tx = _x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx] and board[ty][tx] != 1:
                visited[ty][tx] = True
                if client_board[ty][tx] == -1:
                    q.append((ty, tx, d+1))
                else:
                    if take != 0 and take[0] == d+1:
                        if client[take[1]][0] > ty:
                            take = (d+1, client_board[ty][tx])
                        elif client[take[1]][0] == ty and client[take[1]][1] > tx:
                            take = (d+1, client_board[ty][tx])
                    elif take == 0:
                        take = (d+1, client_board[ty][tx])
    if take == 0:
        return -1
    return take  # (사용 연료, 손님 번호)


def drive(y, x, m):
    ans_y, ans_x = client[m][2], client[m][3]
    if y == ans_y and x == ans_x:
        return 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[y][x] = True
    q = deque()
    q.append((y, x, 0))
    while q:
        _y, _x, d = q.popleft()
        for i in range(4):
            ty = _y + dy[i]
            tx = _x + dx[i]
            if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx] and board[ty][tx] != 1:
                if ty == ans_y and tx == ans_x:
                    return d+1
                else:
                    visited[ty][tx] = True
                    q.append((ty, tx, d+1))
    return -1

cnt = 0
while cnt < M:
    result = taking_client(r, c)
    if result == -1:
        cnt = -1
        break
    else:
        want, no = result
        if fuel - want < 0:
            cnt = -1
            break
        else:
            fuel -= want
            go_y, go_x = client[no][0], client[no][1]
            result = drive(go_y, go_x, no)
            if result == -1:
                cnt = -1
                break
            else:
                if fuel - result < 0:
                    cnt = -1
                    break
                else:
                    fuel += result
                    cnt += 1
                    client_board[go_y][go_x] = -1
                    r = client[no][2]
                    c = client[no][3]
if cnt == M:
    print(fuel)
else:
    print(-1)
