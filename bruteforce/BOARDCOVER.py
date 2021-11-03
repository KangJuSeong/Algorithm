import sys
input = sys.stdin.readline



BLOCK_CASE = [[(0,0),(0,1),(1,0)], [(0,0),(0,1),(1,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,-1)]]


def next():
    for y_i, y in enumerate(map):
        for x_i, x in enumerate(y):
            if not map[y_i][x_i]:
                return y_i, x_i
    return -1, -1

def check_block(y, x, case):
    for _y, _x in BLOCK_CASE[case]:
        ny = y + _y
        nx = x + _x
        if not (0 <= nx < w and 0 <= ny < h): return False
        if map[ny][nx] == 1: return False
    return True

def fill_block(y, x, case):
    for _y, _x in BLOCK_CASE[case]:
        ny = y + _y
        nx = x + _x
        map[ny][nx] = 1

def remove_block(y, x, case):
    for _y, _x in BLOCK_CASE[case]:
        ny = y + _y
        nx = x + _x
        map[ny][nx] = 0

def count_blcok():
    y, x = next()
    if y is -1 and x is -1:
        return 1
    ret = 0
    for i, v in enumerate(BLOCK_CASE):
        if check_block(y, x, i):
            fill_block(y, x, i)
            ret += count_blcok()
            remove_block(y, x, i)
    return ret



C = int(input())
for _ in range(C):
    h, w = map(int, input().split())
    map = []

    space_cnt = 3
    for i in range(h):
        line = list(input().rstrip())
        _line = []
        for j in line:
            if j == '#':
                _line.append(1)
            else:
                space_cnt += 1
                _line.append(0)
        map.append(_line)
    if space_cnt % 3 != 0: print(0)
    else: print(count_blcok())