import sys
input = sys.stdin.readline


N = int(input())
k = int(input())

"""
1 2 3
2 4 6
3 6 9
"""
start = 1
end = k
answer = 0
while start <= end:
    mid = int((start + end) / 2)
    sum = 0
    for i in range(1, N+1):
        sum += min(int(mid/i), N)
    if sum < k:
        start = mid + 1
    else:
        answer = mid 
        end = mid - 1
print(answer)
