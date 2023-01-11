import sys
input = sys.stdin.readline


N = int(input())
cnt = 1
start = 1
end = 1
sum = 1

while end != N:
    if sum < N:
        end += 1
        sum += end
    elif sum > N:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end
        cnt += 1
print(cnt)