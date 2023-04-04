import sys
input = sys.stdin.readline


# 0 = 빈칸, 1 = 집, 2 = 치킨집
N, M = map(int, input().split())
home = list()
chicken = list()

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        loc = (i, j)
        if tmp[j] == 1:
            home.append(loc)
        elif tmp[j] == 2:
            chicken.append(loc)

ans = N * 2 * len(home)

def solution(q):
    global ans
    sum = 0
    for h in home:
        dist = 101
        for c in q:
            r1, c1 = c
            r2, c2 = h
            dist = min(dist, abs(r1-r2) + abs(c1-c2))
        sum += dist
    ans = min(sum, ans)

def dfs(q, d):
    if len(q) == M:
        solution(q)
        return
    elif d == len(chicken):
        return
    q.append(chicken[d])
    dfs(q, d+1)
    q.pop()
    dfs(q, d+1)

dfs(list(), 0)
print(ans)

