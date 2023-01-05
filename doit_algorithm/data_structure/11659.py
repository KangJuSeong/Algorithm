import sys


input = sys.stdin.readline
s, q = map(int, input().split())
n = list(map(int, input().split()))
sum_lst = [0]
s = 0

for i in n:
    s = s + i
    sum_lst.append(s)

for i in range(q):
    a, b = map(int, input().split())
    print(sum_lst[b] - sum_lst[a-1])