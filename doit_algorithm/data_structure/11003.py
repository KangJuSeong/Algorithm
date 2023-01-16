import sys
from collections import deque
input = sys.stdin.readline


N, L = map(int, input().split())
A = list(map(int, input().split()))
D = deque()

for i in range(N):
    while D and D[-1][0] > A[i]:
        D.pop()
    D.append((A[i], i))
    if D[0][1] <= i-L:
        D.popleft()
    print(f"{D[0][0]} ", end='')
    
