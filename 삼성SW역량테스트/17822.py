import sys
input = sys.stdin.readline
from collections import deque
"""
번호가 xi의 배수인 원판을 di방향으로 ki칸 회전시킨다. di가 0인 경우는 시계 방향, 1인 경우는 반시계 방향이다.
원판에 수가 남아 있으면, 인접하면서 수가 같은 것을 모두 찾는다.
    그러한 수가 있는 경우에는 원판에서 인접하면서 같은 수를 모두 지운다.
    없는 경우에는 원판에 적힌 수의 평균을 구하고, 평균보다 큰 수에서 1을 빼고, 작은 수에는 1을 더한다.
"""

n, m, t = map(int, input().split())
disk = [deque(list(map(int, input().split()))) for _ in range(n)]
cmd = list()
dy, dx = (0, 0, -1, 1), (1, -1, 0, 0)
for _ in range(t):
    x, d, k = map(int, input().split())
    cmd.append((x, d, k))

def rotation(x, d, k):
    for i in range(n):
        if (i+1) % x == 0:
            k = k % m
            for _ in range(k):
                if d == 0:
                    disk[i].appendleft(disk[i].pop())
                else:
                    disk[i].append(disk[i].popleft())


def printing(map):
    for i in range(n):
        for j in range(m):
            print(f'{map[i][j]} ', end='')
        print()
    print()


def bfs(y, x):
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    q.append((y, x))
    visited[y][x] = True
    flag = False
    while q:
        _y, _x = q.popleft()
        for i in range(4):
            ty = _y + dy[i]
            tx = _x + dx[i]
            if ty < 0 or ty >= n:
                continue
            if tx < 0:
                tx = m-1
            if tx >= m:
                tx = 0
            if not visited[ty][tx] and disk[ty][tx] == disk[_y][_x]:
                flag = True
                visited[ty][tx] = True
                q.append((ty, tx))
    if flag:
        for r in range(n):
            for c in range(m):
                if visited[r][c]:
                    disk[r][c] = -1
    return flag

total = 0
for x, d, k in cmd:
    rotation(x, d, k)
    cnt = 0
    for r in range(n):
        for c in range(m):
            if disk[r][c] != -1:
                flag = bfs(r, c)
                if not flag:
                    cnt += 1
            else:
                cnt += 1
    if cnt == n * m:
        avg = 0
        a = 0
        for r in range(n):
            for c in range(m):
                if disk[r][c] != -1:
                    avg += disk[r][c]
                    a += 1
        if avg != 0:
            avg = avg / a
        for r in range(n):
            for c in range(m):
                if disk[r][c] != -1:
                    if avg > disk[r][c]:
                        disk[r][c] += 1
                    elif avg < disk[r][c]:
                        disk[r][c] -= 1
                
for r in range(n):
    for c in range(m):
        if disk[r][c] != -1:
            total += disk[r][c]

print(total)
    