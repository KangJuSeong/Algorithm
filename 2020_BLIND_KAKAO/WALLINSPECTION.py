"""
n	weak	          dist	        result
12	[1, 5, 6, 10]	  [1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]  [3, 5, 7]	    1
"""

# N = 12
# WEAK = [1, 3, 4, 9, 10]
# DIST = [3, 5, 7]
# RESULT = 1

N = 12
WEAK = [1, 5, 6, 10]
DIST = [1, 2, 3, 4]
RESULT = 2


def minDist(n, start, end):
    return min(end-start, n-end-start)

def caseNum(weak, n):
    case = list()
    """
    한번에 n개 지점을 가는 경우
    여러번 n-1개 지점을 가는 경우
    """
    for i in range(len(weak)):
        print(i)

    return 1

def checkDist():
    return 1

def solution(n, weak, dist):
    answer = 0
    return answer

if __name__ == '__main__':
    answer = solution(N, WEAK, DIST)
    if answer == RESULT:
        print("OK")
    else:
        print("NO")