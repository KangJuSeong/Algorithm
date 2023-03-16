import sys
input = sys.stdin.readline


N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0

for i in range(N):
    k = A[i] - B
    ans += 1
    if k > 0:
        if k % C:
            ans = ans + k // C + 1
        else:
            ans += k // C
print(ans)