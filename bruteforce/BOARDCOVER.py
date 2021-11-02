import sys

input = sys.stdin.readline


if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        h, w = map(int, input().split())
        map = []
        for i in range(h):
            line = list(input())
            line.pop()
            map.append(line)
        space_cnt = 0
        for i in map:
            for j in i:
                if j == '.':
                    space_cnt += 1
        if space_cnt % 3 != 0:
            print(0)
            continue
        
        