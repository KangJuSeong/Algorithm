import sys
input = sys.stdin.readline

# 0은 청소 x, 1은 청소 o
# 위는 0, 오른쪽 1, 아래는 2, 왼쪽 3
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)

N, M = map(int, input().split())
y, x, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(y, x):
    for dir in range(4):
        

def move(y, x):
    
