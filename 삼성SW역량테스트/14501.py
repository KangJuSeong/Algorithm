import sys
input = sys.stdin.readline


N = int(input())
schedule = list()
for i in range(N):
    a, b = map(int, input().split())
    schedule.append((a, b))
dp = [0 for _ in range(N+1)]
for i in range(N):
    for j in range(i+schedule[i][0], N+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
            
print(dp[-1])