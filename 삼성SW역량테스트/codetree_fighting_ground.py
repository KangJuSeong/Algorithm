# 플레이어 -> 플레이어 번호=index, y, x, 방향, 기본, 총, 점수(총 + 기본의 차이만큼 증가)
# 총 배열(여러개), 플레이어 맵 2개
# 이동 시

# 총 중에서 가장 쎈 총으로 교체
# 밖이면 반대로 변경

# 플레이어라면
# 1. 싸워서 이긴 점수 얻기 (점수가 동일하면 초기 능력치)
# 2. 지면 원래 자리에 총 놓고 이동 -> 벽 또는 플레이어 있으면 90도 회전


dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)
n, m, k = map(int, input().split())  # 격자크기, 플레이어 수, 라운드 수
gun = [[[] for _ in range(n)] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, v in enumerate(tmp):
        gun[i][j].append(v)
players = [[] for _ in range(m+1)]
board = [[0]*n for _ in range(n)]
for _m in range(1, m+1):
    y, x, d, s = map(int, input().split())
    players[_m] = [y, x, d, s, 0, 0]  # y, x, 방향, 기본, 총, 점수(총 + 기본의 차이만큼 증가)
    board[y-1][x-1] = _m


# p1과 p2가 싸웠을 때 이긴 사람을 앞에 리턴
def fight(p1, p2):
    p1_s, p1_g = p1[3], p1[4]
    p2_s, p2_g = p2[3], p2[4]
    point = abs((p1_s + p1_g) - (p2_s, p2_g))
    if p1_s + p1_g > p2_s + p2_g:  # p1이 이겼을 때
        p1[5] += point
        return p1, p2
    elif p1_s + p1_g < p2_s + p2_g:  # p2이 이겼을 때
        p2[5] += point
        return p2, p1
    else:  # 비겼을 떄
        if p1_s > p2_s:  # p1이 이겼ㅇㄹ 때
            p1[5] += point
            return p1, p2
        else:
            p2[5] += point
            return p2, p1


def pick_gun(my, y, x):
    for i, v in enumerate(gun[y][x]):
        if my < v:
            gun[y][x] = my
            my = v
    return my


def move(p):
    y, x, d = p[0], p[1], p[2]
    


# 라운드 실행
while k!=0:
    for p in range(1, m+1):
        print(p) # player 플레이 실행
    k -= 1
