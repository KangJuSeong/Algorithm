from itertools import combinations

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

def solution(n, weak, dist):
    answer = 0
    return answer

if __name__ == '__main__':
    answer = solution(N, WEAK, DIST)
    if answer == RESULT:
        print("OK")
    else:
        print("NO")