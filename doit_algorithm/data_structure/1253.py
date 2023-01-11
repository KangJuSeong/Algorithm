import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))

A.sort()
cnt = 0

for i, v in enumerate(A):
    start = 0
    end = N-1   
    while start != end:
        if A[start] + A[end] == v:
            if start != i and end != i:
                cnt += 1
                break
            elif start == i:
                start += 1
            else:
                end -= 1
        elif A[start] + A[end] < v:
            start += 1
        else:
            end -= 1
print(cnt)