import sys
input = sys.stdin.readline


dy, dx = (0, 1, 0, -1), (-1, 0, 1, 0)
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
arrow = [[(-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), 
         (1, 0, 0.07), (-1, 1, 0.01), (1, 1, 0.01),
         (-1, -1, 0.1), (1, -1, 0.1), (0, -2, 0.05)],

         [(0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), 
         (0, -1, 0.07), (-1, 1, 0.01), (-1, -1, 0.01),
         (1, 1, 0.1), (1, -1, 0.1), (2, 0, 0.05)],
         
         [(-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), 
         (1, 0, 0.07), (-1, -1, 0.01), (1, -1, 0.01),
         (-1, 1, 0.1), (1, 1, 0.1), (0, 2, 0.05)],
         
         [(0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), 
         (0, -1, 0.07), (1, 1, 0.01), (1, -1, 0.01),
         (-1, 1, 0.1), (-1, -1, 0.1), (-2, 0, 0.05)]
         ]  # (날린 모래 y, 날린 모래 x, 먼지 비율)
y, x = N//2, N//2
ans = 0


def spread(r, c, d):
    global ans
    sand = board[r][c]
    total = 0
    for _r, _c, ratio in arrow[d]:
        spread_sand = int(sand * ratio)
        if 0 <= r+_r < N and 0 <= c+_c < N:
            board[r+_r][c+_c] += spread_sand
        else:
            ans += spread_sand
        total += spread_sand
    board[r][c] = 0
    ty, tx = r+dy[d], c+dx[d]
    if 0 <= ty < N and 0 <= tx < N:
        board[ty][tx] += (sand - total)
    else:
        ans += (sand - total)


def printing(map, n):
    for i in range(n):
        for j in range(n):
            print(f'{map[i][j]} ', end='')
        print()
    print()


def storm():
    global y, x
    s = 1
    d = 0
    count = 0
    while y != 0 or x != 0:
        if count == 2:
            s +=1
            count = 0
        for i in range(s):
            y += dy[d]
            x += dx[d]
            if x < 0:
                y = 0
                x = 0
            spread(y, x, d)
        count += 1
        d = (d+1) % 4

storm()
print(ans)