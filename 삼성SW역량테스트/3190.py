import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
K = int(input())
dy, dx = 0, 1
board = [[0]*N for _ in range(N)]
q = deque()
# D 눌렀을 떄 (0,1)->(1,0) (1,0)->(0,-1) (0,-1)->(-1, 0), (-1,0)->(0,1)
# C 눌렀을 떄 (0,1)->(-1,0) (-1,0)->(0,-1) (0,-1)->(1, 0), (1,0)->(0,1)
arrows = dict() # C가 왼쪽 -> , D가 오른쪽
for i in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
L = int(input())
for i in range(L):
    a, b = input().split()
    arrows[int(a)] =  b

def head(dy, dx, arrow):
    if arrow == 'D':
        if dy==0 and dx==1: return 1, 0
        elif dy==1 and dx==0: return 0, -1
        elif dy==0 and dx==-1: return -1, 0
        else: return 0, 1
    else:
        if dy==0 and dx==1: return -1, 0
        elif dy==1 and dx==0: return 0, 1
        elif dy==0 and dx==-1: return 1, 0
        else: return 0, -1

def print_board():
    for i in range(N):
        for j in range(N):
            print(f'{board[i][j]} ', end='')
        print()

y, x = 0, 0
board[y][x] = 2
ans = 0
q.append((y, x))

while True:
    ans += 1
    y += dy
    x += dx
    if x < 0 or x >= N or y < 0 or y >= N:
        break
    if board[y][x] == 1:
        board[y][x] = 2
        q.append((y, x))
        if ans in arrows:
            dy, dx = head(dy, dx, arrows[ans])
    elif board[y][x] == 0:
        board[y][x] = 2
        q.append((y, x))
        ty, tx = q.popleft()
        board[ty][tx] = 0
        if ans in arrows:
            dy, dx = head(dy, dx, arrows[ans])
    else:
        break
print(ans)
        