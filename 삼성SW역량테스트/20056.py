import sys
input = sys.stdin.readline


dy, dx = (-1, -1, 0, 1, 1, 1, 0, -1), (0, 1, 1, 1, 0, -1, -1, -1)
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
fire = list()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())  # y, x, 질량, 속력, 방향
    board[r-1][c-1].append((m, s, d))
    fire.append((r-1, c-1, m, s, d))


def printing(map):
    for i in range(N):
        for j in range(N):
            print(f'{map[i][j]} ', end='')
        print()
    print()


def move(fireball):
    next_fireball = list()
    tmp = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in fireball:
        y = r + dy[d] * s
        x = c + dx[d] * s
        y = (y+N) % N
        x = (x+N) % N
        tmp[y][x].append((m, s, d))
    for i in range(N):
        for j in range(N):
            size = len(tmp[i][j])
            if size == 1:
                m, s, d = tmp[i][j][0][0], tmp[i][j][0][1], tmp[i][j][0][2]
                next_fireball.append((i, j, m, s, d))
            elif size > 1:
                _m = 0
                _s = 0
                _d = 0
                for m, s, d in tmp[i][j]:
                    _m += m
                    _s += s
                    _d += d % 2
                if _m // 5 != 0:
                    tmp[i][j].clear()
                    if _d == size or _d == 0:
                        for k in range(0, 7, 2):
                            next_fireball.append((i, j, _m//5, _s//size, k))
                            tmp[i][j].append((_m//5, _s//size, k))
                    else:
                        for k in range(1, 8, 2):
                            next_fireball.append((i, j, _m//5, _s//size, k))
                            tmp[i][j].append((_m//5, _s//size, k))
                else:
                    tmp[i][j].clear()
    return next_fireball, tmp


for k in range(K):
    fire, board = move(fire)
ans = 0
for i in range(N):
    for j in range(N):
        if board[i][j]:
            for m, s, d in board[i][j]:
                ans += m
print(ans)

                

