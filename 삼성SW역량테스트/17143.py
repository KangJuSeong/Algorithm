import sys
input = sys.stdin.readline


R, C, M = map(int, input().split())
shark = list()
# (r,c) 에 존재, s=속력, d=이동방향, z=크기
# d -> 1=위, 2=아래, 3=오른쪽, 4=왼쪽
dy, dx = (0, -1, 1, 0, 0), (0, 0, 0, 1, -1)
board = [[0] * C for _ in range(R)]
for m in range(M):
    r, c, s, d, z = map(int, input().split())
    shark.append((r-1, c-1, s, d, z))
    board[r-1][c-1] = z


def move_king(k):
    global shark
    survive_shark = list()
    catch_shark = list()
    size = 0
    for sh in shark:
        if sh[1] == k:
            catch_shark.append(sh)
        else:
            survive_shark.append(sh)
    catch_shark = sorted(catch_shark, key=lambda x: x[0])
    for i, sh in enumerate(catch_shark):
        if i == 0:
            size = sh[4]
            board[sh[0]][sh[1]] = 0
        else:
            survive_shark.append(sh)
    shark = survive_shark
    return size
        


def move_shark():
    global shark, board
    tmp = [[list() for _ in range(C)] for _ in range(R)]
    board = [[0] * C for _ in range(R)]
    survive_shark = list()
    for i in range(len(shark)):
        r, c, s, d, z = shark[i]
        _r, _c = r, c
        sec = 0
        while sec < s:
            ty, tx = r + dy[d], c + dx[d]
            if 0 <= ty < R and 0 <= tx < C:
                r = ty
                c = tx
                sec += 1
            else:
                if d == 1: d = 2
                elif d == 2: d =1
                elif d == 3: d=4
                else: d=3
        tmp[r][c].append((z, s, d))
    for r in range(R):
        for c in range(C):
            if tmp[r][c]:
                z, s, d = max(tmp[r][c])
                board[r][c] = z
                survive_shark.append((r, c, s, d, z))
    shark = survive_shark


def print_board():
    for r in range(R):
        for c in range(C):
            print(f'{board[r][c]} ', end='')
        print()
    print()

ans = 0
for c in range(C):
    catch = move_king(c)
    if catch:
        ans += catch
    move_shark()

print(ans)