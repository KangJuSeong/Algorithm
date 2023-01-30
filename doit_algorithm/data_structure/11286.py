import sys
input = sys.stdin.readline
from queue import PriorityQueue

N = int(input())

Q = PriorityQueue()

for i in range(N):
    a = int(input())
    if a == 0:
        if Q.empty():
            print('0')
        else:
            tmp = Q.get()
            print(str((tmp[1])))
    else:
        Q.put((abs(a), a))