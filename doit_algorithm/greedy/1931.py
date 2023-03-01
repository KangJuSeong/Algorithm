# import sys
# input = sys.stdin.readline


# N = int(input())
# A = list()
# for i in range(N):
#     a, b = map(int, input().split())
#     A.append((a, b))
# A.sort(key=lambda x: x[1])
# print(A)
# cnt = 0
# end = -1
# for i in A:
#     if i[0] >= end:
#         end = i[1]
#         cnt += 1
# print(cnt)

import sys
input = sys.stdin.readline

N = int(input())
A = [[0] * 2 for _ in range(N)]
for i in range(N):
    S, E = map(int, input().split())
    A[i][0] = E
    A[i][1] = S
A.sort()
cnt = 0
end = -1
for i in range(N):
    if A[i][1] >= end:
        end = A[i][0]
        cnt += 1
        
print(cnt)