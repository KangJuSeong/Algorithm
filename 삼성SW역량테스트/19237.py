import sys
input = sys.stdin.readline
from collections import deque

# 1. 비어있는 칸, 2. 자기 냄새 칸 3. 비어있는게 여러개 또는 자기 냄새칸이 여러개이면 우선순위


dy, dx = (0, -1, 1, 0, 0) , (0, 0, 0, -1, 1)
die = list()
N, M, K = map(int, input().split())
def printing(map):
    for i in range(N):
        for j in range(N):
            print(f'{map[i][j]} ', end='')
        print()
    print()
board = [[0 for _ in range(N)] for _ in range(N)]
shark = [[0, 0, 0] for _ in range(M+1)]  # 인덱스 = 상어 번호 [y, x, d] -> 좌표와 방향
smell = [[[0, 0] for _ in range(N)] for _ in range(N)] # 상어 번호, 냄새 시간
for i in range(N):
    s = list(map(int, input().split()))
    for j, v in enumerate(s):
        board[i][j] = v
        if v != 0:
            shark[v][0] = i
            shark[v][1] = j
dlist = list(map(int, input().split()))
for i, v, in enumerate(dlist):
    shark[i+1][2] = v
priority = [[list() for _ in range(5)] for _ in range(M+1)]  # priority[1][1] = [1, 2, 3, 4]
for m in range(M):
    for d in range(4):
        a = list(map(int, input().split()))
        priority[m+1][d+1] = a

depth = 0
cnt = 0
def bfs():
    global depth, cnt
    q = deque()
    for s in range(1, M+1):
        y, x, d = shark[s]
        smell[y][x][0] = s
        smell[y][x][1] = K
        q.append((s, y, x, d, 0))  # 상어번호, y, x, 방향, 시간(초)
    while q:
        n, y, x, d, sec = q.popleft()
        # 0: 갈곳 x, 1: 빈곳, 2: 내 냄새, y, x)
        if n in die:
            continue
        first = list()
        second = list()
        third = list()
        for i in range(1, 5):
            ty = y + dy[i]
            tx = x + dx[i]
            if not (0 <= ty < N and 0 <= tx < N):
                continue
            if smell[ty][tx][1] == 0:
                first.append((ty, tx, i))
            elif smell[ty][tx][0] == n:
                second.append((ty, tx, i))
            else:
                third.append((y, x, d))
        cur = [-1, -1]
        if first:
            if len(first) > 1:
                flag = False
                for i in range(4):
                    for ty, tx, td in first:
                        if td == priority[n][d][i] and not flag:
                            q.append((n, ty, tx, td, sec+1))
                            cur = [ty, tx]
                            flag = True
            else:
                ty, tx, td = first[0]
                q.append((n, ty, tx, td, sec+1))
                cur = [ty, tx]
        elif second:
            if len(second) > 1:
                flag = False
                for i in range(4):
                    for ty, tx, td in second:
                        if td == priority[n][d][i] and not flag:
                            q.append((n, ty, tx, td, sec+1))
                            cur = [ty, tx]
                            flag = True
            else:
                ty, tx, td = second[0]
                q.append((n, ty, tx, td, sec+1))
                cur = [ty, tx]
        else:
            ty, tx, td = third[0]
            q.append((n, ty, tx, td, sec+1))
            cur = [ty, tx]
        s = board[cur[0]][cur[1]] 
        if s != 0 and s > n:
            die.append(s)
            board[cur[0]][cur[1]] = n
        elif s != 0 and s < n:
            die.append(n)
        elif s == 0:
            board[cur[0]][cur[1]] = n
        board[y][x] = 0
        total = 0
        for r in range(N):
            total += sum(board[r])
        if total == 1:
            return depth+1
        if depth+1 > 1000:
            return -1
        cnt += 1
        if cnt == M:
            for r in range(N):
                for c in range(N):
                    if board[r][c] > 0:
                        if not board[r][c] in die:
                            smell[r][c][0] = board[r][c]
                            smell[r][c][1] = K
                        continue
                    if smell[r][c][0] != 0:
                        smell[r][c][1] -= 1
                        if smell[r][c][1] ==0:
                            smell[r][c][0] = 0
            depth = sec+1
            cnt = len(die)
print(bfs())
