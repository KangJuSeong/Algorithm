import sys
input = sys.stdin.readline


A = list(input())

for i in range(len(A)):
    M = i
    for j in range(i+1, len(A)):
        if A[j] > A[M]:
            M = j
    if A[i] < A[M]:
        tmp = A[i]
        A[i] = A[M]
        A[M] = tmp
        
for i in range(len(A)):
    print(A[i], end='')