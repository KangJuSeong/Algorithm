import sys
input = sys.stdin.readline


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 100 * 20 * 20 + 1
"""
(x, y), (x+1, y-1), ..., (x+d1, y-d1)
(x, y), (x+1, y+1), ..., (x+d2, y+d2)
(x+d1, y-d1), (x+d1+1, y-d1+1), ... (x+d1+d2, y-d1+d2)
(x+d2, y+d2), (x+d2+1, y+d2-1), ..., (x+d2+d1, y+d2-d1)

d1, d2 ≥ 1, 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N

1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N
"""


def check(y, x):
    if not 0 <= y < N or not 0 <= x < N:
        return False
    return True


def print_board(board):
    for i in range(N):
        for j in range(N):
            print(f'{board[i][j]} ', end='')
        print()
    print()


def ward(y, x, d1, d2):
    global ans
    board = [[0] * N for _ in range(N)]
    for i in range(d1+1):
        ty = y + i
        tx = x - i
        if not check(ty, tx):
            return
        board[ty][tx] = 5
    for i in range(d2+1):
        ty = y + i
        tx = x + i
        if not check(ty, tx):
            return
        board[ty][tx] = 5
    for i in range(d2+1):
        ty = y + d1 + i
        tx = x - d1 + i
        if not check(ty, tx):
            return
        board[ty][tx] = 5
    for i in range(d1+1):
        ty = y + d2 + i
        tx = x + d2 - i
        if not check(ty, tx):
            return
        board[ty][tx] = 5
    people = [0, 0, 0, 0, 0]
    for r in range(N):
        if sum(board[r]) == 10:
            start = 0
            for c in range(N):
                if not start and board[r][c] == 5:
                    start = 1
                elif start and board[r][c] == 0:
                    board[r][c] = 5
                elif start and board[r][c] == 5:
                    break
    total = 0
    for r in range(N):
        for c in range(N):
            total += A[r][c]
    for r in range(y+d1): # 0 ~ y+d1-1
        for c in range(x+1): # 0 ~ x
            if board[r][c] == 5:
                break
            else:
                people[0] += A[r][c]
    for r in range(y+d2+1): # 0 ~ y+d2
        for c in range(N-1, x, -1): # N-1 ~ x+1
            if board[r][c] == 5:
                break
            else:
                people[1] += A[r][c]
    for r in range(y+d1, N): # y+d1 ~ N-1
        for c in range(x-d1+d2): # 0 ~ x-d1+d2-1
            if board[r][c] == 5:
                break
            else:
                people[2] += A[r][c]
    for r in range(y+d2+1, N): # y+d2+1 ~ N-1
        for c in range(N-1, x-d1+d2-1, -1): # N-1 ~ x-d1+d2-1
            if board[r][c] == 5:
                break
            else:
                people[3] += A[r][c]
    people[4] = total - sum(people)
    
    
    if ans != 15 and max(people) - min(people) == 15:
        print(people)
        print_board(board)
        print_board(A)
    ans = min(ans, max(people) - min(people))


for d1 in range(1, N-1):
    for d2 in range(1, N-1):
        for r in range(N):
            for c in range(N):
                ward(r, c, d1, d2)
print(ans)
