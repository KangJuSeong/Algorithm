import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
start = 0
end = N-1
cnt = 0
sum = 0

while end != start:
    if A[start] + A[end] == M:
        cnt += 1
        end -= 1
    elif A[start] + A[end] < M:
        start += 1
    else:
        end -= 1
print(cnt)