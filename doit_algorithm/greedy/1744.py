from queue import PriorityQueue
import sys
input = sys.stdin.readline


N = int(input())
sum = 0
PQ = PriorityQueue()
MQ = PriorityQueue()
ZC = 0
OC = 0

for _ in range(N):
    d = int(input())
    if d > 1: PQ.put(d * -1)
    if d < 1: MQ.put(d)
    if d == 1: OC += 1
    if d == 0: ZC += 1
    
while PQ.qsize() > 1:
    a, b = PQ.get(), PQ.get()
    sum += (a * -1) * (b * -1)
if not PQ.empty():
    sum += PQ.get() * -1
    
while MQ.qsize() > 1:
    a, b = MQ.get(), MQ.get()
    sum += a * b
if not MQ.empty() and ZC == 0:
    sum += MQ.get()
sum += OC
print(sum)