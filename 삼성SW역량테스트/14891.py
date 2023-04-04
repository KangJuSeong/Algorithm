import sys
input = sys.stdin.readline
# 맞닿는 곳이 극이 다르면 반대 방향으로 회전
# 맞닿는 곳이 극이 같으면 같은 회전 X
# N = 0, S = 1
# 1 = 시계, -1 = 반시계
# 0, 1, 2, 3, 4, 5, 6, 7

gear = list()
for i in range(4):
    a = input()
    gear.append(list(map(int, a[:-1])))
K = int(input())
cmd = [tuple(map(int, input().split())) for _ in range(K)]


def rotation(y, arrow):
    if arrow == 1:
        tmp = gear[y].pop(-1)
        gear[y].insert(0, tmp)
    elif arrow == -1:
        tmp = gear[y].pop(0)
        gear[y].append(tmp)


def check(y, side):  # side : 0 = left, 1 = right
    if side == 0:
        if gear[y][6] != gear[y-1][2]:
            return True
        else:
            return False
    else:
        if gear[y][2] != gear[y+1][6]:
            return True
        else:
            return False


def score():
    ans = 0
    if gear[0][0]:
        ans += 1
    if gear[1][0]:
        ans += 2
    if gear[2][0]:
        ans += 4
    if gear[3][0]:
        ans += 8
    return ans


for a, b in cmd:
    a = a - 1
    c = [0] * 4
    c[a] = b
    if a == 0:
        for i in range(3):
            if check(a+i, 1):
                b *= -1
                c[a+i+1] = b
            else:
                break
    elif a == 1:
        if check(a, 0):
            c[a-1] = b * -1
        for i in range(2):
            if check(a+i, 1):
                b *= -1
                c[a+i+1] = b
            else:
                break
    elif a == 2:
        if check(a, 1):
            c[a+1] = b * -1
        for i in range(2):
            if check(a-i, 0):
                b *= -1
                c[a-i-1] = b
            else:
                break
    else:
        for i in range(3):
            if check(a-i, 0):
                b *= -1
                c[a-i-1] = b
            else:
                break
    for i, v in enumerate(c):
        rotation(i, v)
print(score())
