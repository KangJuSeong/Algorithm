import sys
input = sys.stdin.readline
from copy import deepcopy


N = int(input())
M = list()
ans = 0
# 0은 위, 1은 오른쪽, 2는 아래, 3은 왼쪽
visited = [[False] * N for _ in range(N)]
for i in range(N):
    M.append(list(map(int, input().split())))

def move(_map, arrow):
    if arrow == 0:
        for x in range(N):
            top = 0
            for y in range(1, N):
                if _map[y][x]:
                    tmp = _map[y][x]
                    _map[y][x] = 0
                    if _map[top][x] == tmp:
                        _map[top][x] = tmp * 2
                        top += 1
                    elif _map[top][x] == 0:
                        _map[top][x] = tmp
                    else:
                        top += 1
                        _map[top][x] = tmp

    elif arrow == 1:
        for y in range(N):
            top = N - 1
            for x in range(N-2, -1, -1):
                    if _map[y][x]:
                        tmp = _map[y][x]
                        _map[y][x] = 0
                        if _map[y][top] == tmp:
                            _map[y][top] = tmp * 2
                            top -= 1
                        elif _map[y][top] == 0:
                            _map[y][top] = tmp
                        else:
                            top -= 1
                            _map[y][top] = tmp

    elif arrow == 2:
        for x in range(N):
            top = N - 1
            for y in range(N-2, -1, -1):
                if _map[y][x]:
                    tmp = _map[y][x]
                    _map[y][x] = 0
                    if _map[top][x] == tmp:
                        _map[top][x] = tmp * 2
                        top -= 1
                    elif _map[top][x] == 0:
                        _map[top][x] = tmp
                    else:
                        top -= 1
                        _map[top][x] = tmp
    elif arrow == 3:
        for y in range(N):
            top = 0
            for x in range(1, N):
                if _map[y][x]:
                    tmp = _map[y][x]
                    _map[y][x] = 0
                    if _map[y][top] == tmp:
                        _map[y][top] = tmp * 2
                        top += 1
                    elif _map[y][top] == 0:
                        _map[y][top] = tmp
                    else:
                        top += 1
                        _map[y][top] = tmp
    return _map

def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, board[i][j])
        return
    
    for arrow in range(4):
        dfs(move(deepcopy(board), arrow), cnt + 1)
        
dfs(M, 0)
print(ans)