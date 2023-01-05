import sys
input = sys.stdin.readline


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sum = 0
a = 0
sum_arr = []
C = [0] * m
for i in numbers:
    sum += i
    t = sum % m
    if t == 0:
        a += 1
    C[t] += 1
    sum_arr.append(t)   

for i in range(m):
    if C[i] > 0:
        a += (C[i] * (C[i]-1) // 2)
print(a)