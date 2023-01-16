import sys
input = sys.stdin.readline


S, P = map(int, input().split())
DNA = input()
# A C G T
A, C, G, T = map(int, input().split())

answer = 0
start = 0
end = P-1
check = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

def counting(c):
    global check
    check[c] += 1
    
def _counting(c):
    global check
    check[c] -= 1
    
def correct():
    global check, answer
    if A <= check['A'] and C <= check['C'] and G <= check['G'] and T <= check['T']:
        answer += 1

for i in range(end+1):
    counting(DNA[i])
correct()
_counting(DNA[start])
start += 1
end += 1
while end < S:
    counting(DNA[end])
    correct()
    _counting(DNA[start])
    start += 1
    end += 1
print(answer)
    