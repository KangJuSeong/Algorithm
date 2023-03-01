import sys
input = sys.stdin.readline


N, K = map(int, input().split())
A = list()
for _ in range(N):
    A.append(int(input()))

coin = 0

for i in range(N-1, -1, -1):
    if A[i] <= K:
        coin = coin + int(K / A[i])
        K = K % A[i]
print(coin)
     
