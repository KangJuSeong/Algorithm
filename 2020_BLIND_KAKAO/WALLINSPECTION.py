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
    W, F = len(weak), len(dist)
    repair_lst = [()]
    count = 0
    dist.sort(reverse=True)

    for can_move in dist:
        repairs = []
        count += 1

        for i, wp in enumerate(weak): # [1 5 6 10]
            start = wp
            ends = weak[i:] + [n+w for w in weak[:i]]
            can = [end % n for end in ends if end-start <= can_move]
            repairs.append(set(can))
        
        cand = set()
        for r in repairs:
            for x in repair_lst:
                new = r | set(x)
                if len(new) == W:
                    return count
                cand.add(tuple(new))
        repair_lst = cand
    return -1