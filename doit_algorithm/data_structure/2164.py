import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
card = deque(list(range(N, 0, -1)))

while len(card) != 1:
    card.pop()
    card.appendleft(card.pop())
print(card.pop())

