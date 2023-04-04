import sys
from copy import deepcopy
input = sys.stdin.readline
# 1번 = 한쪽, 2번 = 한쪽과 반대, 3번 = 한쪽과 90도, 4번 = 한쪽과 좌우 90도, 5번 = 전체, 6번 = 벽


N, M = map(int, input().split())
ans = 65
board = list([0] * M for _ in range(N))
cctv = list()
for i in range(N):
    a = list(map(int, input().split()))
    for j, v in enumerate(a):
        if v != 0 and v != 6:
            cctv.append((i, j, v))
        board[i][j] = v
cctv_dict = {
    1: [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],
    2: [(1, 1, 0, 0), (0, 0, 1, 1)],
    3: [(1, 0, 1, 0), (1, 0, 0, 1), (0, 1, 0, 1), (0, 1, 1, 0)],
    4: [(1, 1, 1, 0), (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1)],
    5: [(1, 1, 1, 1)]
}


def line(_board, arrow, y, x):
    left, right, up, down = arrow
    if left:
        for i in range(1, x+1):
            if _board[y][x-i] == 6:
                break
            elif _board[y][x-i] == 0:
                _board[y][x-i] = 7
            else:
                continue
    if up:
        for i in range(1, y+1):
            if _board[y-i][x] == 6:
                break
            elif _board[y-i][x] == 0:
                _board[y-i][x] = 7
            else:
                continue
    if right:
        for i in range(1, M-x):
            if _board[y][x+i] == 6:
                break
            elif _board[y][x+i] == 0:
                _board[y][x+i] = 7
            else:
                continue
    if down:
        for i in range(1, N-y):
            if _board[y+i][x] == 6:
                break
            elif _board[y+i][x] == 0:
                _board[y+i][x] = 7
            else:
                continue
    return _board


def score(_board):
    tmp = 0
    for i in range(N):
        for j in range(M):
            if _board[i][j] == 0:
                tmp += 1
    return tmp


def print_board(_board):
    for i in range(N):
        for j in range(M):
            print(f'{_board[i][j]} ', end='')
        print()
    print()


def dfs(idx, map):
    global ans
    if idx == len(cctv):
        ans = min(ans, score(map))
        return
    y, x, num = cctv[idx]
    for i, v in enumerate(cctv_dict[num]):
        dfs(idx+1, line(deepcopy(map), v, y, x))

dfs(0, board)
print(ans)
