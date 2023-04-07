import sys
input = sys.stdin.readline
from copy import deepcopy


dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, -1, -1, -1, 0, 1, 1, 1)

board = [[[0, 0] for _ in range(4)] for _ in range(4)]  # 번호, 방향, y, x
for i in range(4):
    a = list(map(int, input().split()))
    k = 0
    for j in range(0, 8, 2):
        board[i][k][0] = a[j]
        board[i][k][1] = a[j+1]-1
        k += 1
max_score = 0


def printing(map):
    for i in range(4):
        for j in range(4):
            print(f'{map[i][j]} ', end='')
        print()
    print()



def dfs(y, x, score, map):
    global max_score
    score += map[y][x][0]
    max_score = max(max_score, score)
    map[y][x][0] = 0
    
    for i in range(16):
        r, c = -1, -1
        for _r in range(4):
            for _c in range(4):
                if map[_r][_c][0] == i+1:
                    r, c = _r, _c
                    break
        if r == -1 and c == -1:
            continue
        arrow = map[r][c][1]
        for i in range(8):
            _arrow = (arrow+i) % 8
            ty = r + dy[_arrow]
            tx = c + dx[_arrow]
            if not (0 <= ty < 4 and 0 <= tx < 4) or (ty == y and tx == x):
                continue
            map[r][c][1] = _arrow
            map[r][c], map[ty][tx] = map[ty][tx], map[r][c]
            break

    arrow = map[y][x][1]
    for i in range(1, 5):
        ty = y + dy[arrow]*i
        tx = x + dx[arrow]*i
        if 0 <= ty < 4 and 0 <= tx < 4 and map[ty][tx][0] != 0:
            dfs(ty, tx, score, deepcopy(map))


dfs(0, 0, 0, board)
print(max_score)


