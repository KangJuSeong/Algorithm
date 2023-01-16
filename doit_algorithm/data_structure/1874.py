import sys
input = sys.stdin.readline


N = int(input())
A = list()
B = list()
C = list()
for _ in range(N):
    A.append(int(input()))
n = 1
flag = 1
for i in range(N):
    while n <= A[i]:
        B.append(n)
        C.append('+')
        n += 1
    k = B.pop()
    if k == A[i]:
        C.append('-')
    else:
        flag = 0
        break
if flag:
    for i in C:
        print(f"{i}")
else:
    print("NO")
    
