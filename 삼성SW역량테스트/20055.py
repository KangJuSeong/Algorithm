import sys
input = sys.stdin.readline
from collections import deque


N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))


robot = deque([False] * N)
ans = 1


def printing(arr):
    for i in range(N):
        print(f'[{arr[i]}] ', end='')
    print()
    for i in range(2*N-1, N-1, -1):
        print(f'[{arr[i]}]', end='')
    print()       


def rotate():
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())


while True:
    rotate()
    robot[-1] = False
    for i in range(N-2, -1, -1):
        if robot[i] and not robot[i+1] and belt[i+1] >= 1:
            robot[i+1] = True
            robot[i] = False
            belt[i+1] -= 1
    robot[-1] = False
    if not robot[0] and belt[0] >= 1:
        belt[0] -= 1
        robot[0] = True
    cnt = 0
    for a in belt:
        if a == 0:
            cnt += 1
    if cnt >= K:
        break
    ans += 1
print(ans)