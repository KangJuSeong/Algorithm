import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))
_min = 1000000000
_max = -1000000000
        
def _dfs(d, t, plus, minus, mul, div):
    global _min, _max
    if d == N-1:
        _max = max(t, _max)
        _min = min(t, _min)
        return
    if plus:
        _dfs(d+1, t+arr[d+1], plus-1, minus, mul, div)
    if minus:
        _dfs(d+1, t-arr[d+1], plus, minus-1, mul, div)
    if mul:
        _dfs(d+1, t*arr[d+1], plus, minus, mul-1, div)  
    if div:
        _dfs(d+1, int(t/arr[d+1]), plus, minus, mul, div-1)

_dfs(0, arr[0], op[0], op[1], op[2], op[3])
print(_max)
print(_min)
