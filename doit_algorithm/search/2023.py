import sys
input = sys.stdin.readline


N = int(input())

def isPrime(num):
    for i in range(2, int(num/2+1)):
        if num % i == 0:
            return False
    return True


def dfs(num):
    global N
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(num * 10 + i):
                dfs(num * 10 + i)
                
dfs(2)
dfs(3)
dfs(5)
dfs(7)