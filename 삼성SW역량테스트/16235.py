import sys
input = sys.stdin.readline
from collections import deque
"""
봄 -> 자신의 나이만큼 양분 먹고 나이 1 증가, 나이가 어린 나무부터 양분 섭취, 양분 부족한 나무는 즉사
여름 -> 봄에 죽은 나무가 양분, 죽은 나무의 나이를 2로 나눈 값이 양분 (소수 버림)
가을 -> 나무가 번식, 번식하는 나무의 나이는 5의 배수, 인접한 8개 칸에 나이가 1인 나무 생성
겨울 -> 각 칸에 양분 추가, 양분의 양은 A[r][c](입력)
"""


dx, dy = (0, 0, 1, -1, 1, -1, -1, 1), (1, -1, 0, 0, -1, 1, -1, 1)
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree = [[deque() for _ in range(N)] for _ in range(N)]
food = [[5 for _ in range(N)] for _ in range(N)]

for i in range(M):
    y, x, z = map(int, input().split())
    tree[y-1][x-1].append(z)

def spring_summer():
    for y in range(N):
        for x in range(N):
            for t in range(len(tree[y][x])):
                total = food[y][x]
                age = tree[y][x][t]
                if total-age >= 0:
                    food[y][x] -= age
                    tree[y][x][t] += 1
                else:
                    while len(tree[y][x]) != t:
                        feed = tree[y][x].pop()
                        food[y][x] += feed // 2
                    break


def fall():
    for y in range(N):
        for x in range(N):
            for t in range(len(tree[y][x])):
                if tree[y][x][t] % 5 == 0:
                    for i in range(8):
                        ty = y + dy[i]
                        tx = x + dx[i]
                        if 0 <= ty < N and 0 <= tx < N:
                            tree[ty][tx].appendleft(1)


def winter():
    for y in range(N):
        for x in range(N):
            food[y][x] += A[y][x]


def print_tree():
    for i in range(N):
        for j in range(N):
            print(f'{list(tree[i][j])} ', end='')
        print()
    print()

def print_food():
    for i in range(N):
        for j in range(N):
            print(f'{food[i][j]} ', end='')
        print()
    print()


def total():
    s = 0
    for y in range(N):
        for x in range(N):
            s += len(tree[y][x])
    return s   


for _ in range(K):
    spring_summer()
    fall()
    winter()
print(total())