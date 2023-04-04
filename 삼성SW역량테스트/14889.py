import sys
input = sys.stdin.readline


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

player = [i for i in range(N)]
q = list()
ans = N // 2  * 100 + 1

def cal():
    global ans
    a = 0
    b = 0
    for i in range(N//2):
        for j in range(N//2):
            a += S[q[i]][q[j]]
    away = list()
    for i in player:
        if not i in q:
            away.append(i)
    for i in range(N//2):
        for j in range(N//2):
            b += S[away[i]][away[j]]
    ans = min(ans, abs(a-b))
            
    
def dfs(d):
    if len(q) == N//2:
        cal()
        return
    elif d == len(player):
        return
    q.append(player[d])
    dfs(d+1)
    q.pop()
    dfs(d+1)
dfs(0)
print(ans)