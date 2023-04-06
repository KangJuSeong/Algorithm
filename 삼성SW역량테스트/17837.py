import sys
input = sys.stdin.readline
from collections import deque


# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나
# 1번 말부터 K번말 이동 
#흰색은 append = 0, 빨간색은 appendleft = 1, 파란색은 = 2 방향 반대로 하고 이동하는데 또 파란색이면 멈춤 + 체스판 밖은 파란색과 동일
dy, dx = (0, 0, 0, -1, 1), (0, 1, -1, 0, 0) # 1-> 오른쪽 2->왼쪽 3->위쪽 4->아래쪽
cmd = deque() # 체스번호, y, x, 방향
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
chess = [[deque() for _ in range(N)] for _ in range(N)]
for k in range(K):
    r, c, d = map(int, input().split())
    cmd.append([k+1, r-1, c-1, d])
    chess[r-1][c-1].append(k+1)

def printing(map):
    for i in range(N):
        for j in range(N):
            print(f'{map[i][j]} ', end='')
        print()
    print()


def over(q):
    if len(q) == K:
        return True
    else:
        return False
    

def move(n, y, x, d, blue):
    global cmd
    ty = y + dy[d]
    tx = x + dx[d]
    if 0 <= ty < N and 0 <= tx < N:
        total = len(chess[ty][tx])
        if blue and board[ty][tx] == 2:
            if K == 4:
                return -1
            else:
                cmd.append([n, y, x, d])
                return
        if board[ty][tx] == 2:
            if d == 1: d = 2
            elif d == 2: d = 1
            elif d == 3: d = 4
            elif d == 4: d = 3
            return move(n, y, x, d, True)
        elif board[ty][tx] == 1:
            while True:
                c = chess[y][x].pop()
                chess[ty][tx].append(c)
                for k in range(len(cmd)):
                    if cmd[k][0] == c:
                        cmd[k][1] = ty
                        cmd[k][2] = tx
                total += 1
                if total == 4:
                    return 1
                if c == n:
                    break
            cmd.append([n, ty, tx, d])
        elif board[ty][tx] == 0:
            tmp = deque()
            idx = 0
            while True:
                if chess[y][x][idx] == n:
                    break
                else:
                    tmp.append(chess[y][x][idx])
                    idx += 1
            for i in range(idx, len(chess[y][x])):
                chess[ty][tx].append(chess[y][x][i])
                for c in range(len(cmd)):
                    if cmd[c][0] == chess[y][x][i]:
                        cmd[c][1] = ty
                        cmd[c][2] = tx
                total += 1
                if total == 4:
                    return 1
            chess[y][x] = tmp
            cmd.append([n, ty, tx, d])
    else:
        if blue:
            if K == 4:
                return -1
            else:
                cmd.append([n, y, x, d])
                return
        elif d == 1: d = 2
        elif d == 2: d = 1
        elif d == 3: d = 4
        elif d == 4: d = 3
        return move(n, y, x, d, True)

flag = 0
ans = 0
while True:
    for i in range(K):
        n, y, x, d = cmd.popleft()
        flag = move(n, y, x, d, False)
        if flag == -1:
            ans = -1
            break
        if flag == 1:
            break
    if flag == -1:
        break
    if flag == 1:
        ans += 1
        break
    ans += 1
    if ans > 1000:
        ans = -1
        break
print(ans)
