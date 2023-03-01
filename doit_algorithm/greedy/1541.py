import sys
input = sys.stdin.readline

A = list(map(str, input().split('-')))
A[-1] = A[-1][:-1]
ans = 0

def mySum(i):
    sum = 0
    tmp = str(i).split('+')
    for i in tmp:
        sum += int(i)
    return sum

for i in range(len(A)):
    tmp = mySum(A[i])
    if i == 0:
        ans += tmp
    else:
        ans -= tmp
print(ans)