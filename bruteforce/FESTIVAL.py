import sys


input = sys.stdin.readline

test_case = int(input())
result = []

for _ in range(test_case):
    day, team = map(int, input().split())
    day_list = list(map(int, input().split()))
    min_value = 987654321.0
    for i in range(day-team+1):
        days = 1
        cost = 0
        for j in range(i, day):
            cost += day_list[j]
            if days >= team:
                if min_value > cost / days:
                    min_value = cost / days
            days += 1
    print("%.8f" % min_value)