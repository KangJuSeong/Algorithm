import sys
input = sys.stdin.readline


N = int(input())
A = []


for i in range(N):
    A.append((int(input()), i))
    
M = 0
A = sorted(A)

for i in range(N):
    if M < A[i][1] - i:
        M = A[i][1] - i
        
print(M+1)
