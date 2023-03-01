from queue import PriorityQueue
import sys
input = sys.stdin.readline


N = int(input())
Q = PriorityQueue()

for i in range(N):
    Q.put(int(input()))

d1 = 0
d2 = 0
sum = 0

while Q.qsize() > 1:
    d1 = Q.get()
    d2 = Q.get()
    tmp = d1 + d2
    sum += tmp
    Q.put(tmp)
print(sum)
