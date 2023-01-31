import sys
input = sys.stdin.readline


N, M = map(int, input().split())
visited = [False] * (N+1)
A = [[] for _ in range(N+1)]
S = list()

for i in range(M):
    a, b = map(int, input().split())
    A[a].append(b)
    A[b].append(a)
    
result = 0
for idx in range(1, N+1):
    if visited[idx]:
        continue
    else:
        visited[idx] = True
        S.append(idx)
    while S:
        k = S.pop()
        for i in A[k]:
            if visited[i]:
                continue
            S.append(i)
            visited[i] = True
    else:
        result += 1
print(result)