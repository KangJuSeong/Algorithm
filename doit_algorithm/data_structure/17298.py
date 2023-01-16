import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

R = [0] * N
S = list()
S.append(0)
for i in range(1, N):
    while S and A[i] > A[S[-1]]:
        R[S.pop()] = A[i]
    S.append(i)
while S:
    R[S.pop()] = -1
for i in R:
    print(f"{i} ", end='')
    
        