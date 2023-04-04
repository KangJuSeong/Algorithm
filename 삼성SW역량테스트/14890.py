import sys


input = sys.stdin.readline
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0


def check_line(line, runway):
    for i in range(1, N):
        if abs(line[i] - line[i-1]) > 1:
            return False
        if line[i] < line[i-1]:
            for j in range(L):
                if i+j >= N or line[i] != line[i+j] or runway[i+j]:
                    return False
                if line[i] == line[i+j]:
                    runway[i+j] = True
        elif line[i] > line[i-1]:
            for j in range(L):
                if i-j-1 < 0 or line[i-1] != line[i-1-j] or runway[i-j-1]:
                    return False
                if line[i-1] == line[i-j-1]:
                    runway[i-j-1] = True
    return True


for i in range(N):
    if check_line([board[i][j] for j in range(N)], [False] * N):
        ans += 1
for j in range(N):
    if check_line([board[i][j] for i in range(N)], [False] * N):
        ans += 1

print(ans)
