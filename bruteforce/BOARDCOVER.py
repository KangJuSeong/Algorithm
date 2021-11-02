import sys
input = sys.stdin.readline

global result
result = 0

BLOCK_CASE = [(1, 1), (-1, 1), (1, -1), (-1, -1)]


def next(map):
    for y_i, y in enumerate(map):
        for x_i, x in enumerate(y):
            if map[y_i][x_i] == 0:
                return y_i, x_i

def block(map, y, x, h, w):
    global result
    full_cnt = 0
    for i in map:
        for j in i:
            if j == 1:
                full_cnt += 1
    if full_cnt == h*w:
        result += 1
        return 
    if y == h-1 and x == w-1:
        return
    for idx, case in enumerate(BLOCK_CASE):
        if x + case[1] >= 0 and y + case[0] >= 0:
            if map[y][x+case[1]] == 0 and map[y+case[0]][x] == 0:
                _map = []
                for i in map:
                    tmp = []
                    for j in i:
                        tmp.append(j)
                    _map.append(tmp)
                _map[y][x+case[1]] = 1
                _map[y+case[0]][x] = 1
                _map[y][x] = 1
                next_y, next_x = next(_map)
                block(_map, next_y, next_x, h, w)
        else:
            next_y, next_x = next(map)
            block(map, next_y, next_x, h, w)



if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        h, w = map(int, input().split())
        map = []
        space_cnt = 0
        # for i in range(h):
        #     line = list(input())
        #     line.pop()
        #     _line = []
        #     for j in line:
        #         if j == '#':
        #             _line.append(1)
        #         else:
        #             space_cnt += 1
        #             _line.append(0)
        #     map.append(_line)
        map = [[1,0,0,0,0,0,1],
               [1,0,0,0,0,0,1],
               [1,1,0,0,1,1,1]]
        if space_cnt % 3 != 0:
            print(0)
            continue
        start_y, start_x = next(map)
        block(map, start_y, start_x, h, w)
        print(result)
        result = 0