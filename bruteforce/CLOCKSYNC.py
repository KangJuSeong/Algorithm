import sys
input = sys.stdin.readline


SWITCH = {
            0: [0, 1, 2], 1: [3, 7, 9, 11], 2: [4, 10, 14 ,15],
            3: [0, 4, 5, 6, 7], 4: [6, 7, 8, 10, 12], 5: [0, 2, 14, 15],
            6: [3, 14, 15], 7: [4, 5, 7, 14, 15], 8: [1, 2, 3, 4, 5],
            9: [3, 4, 5, 9, 13]
         }


def check_all_twelve(clocks):
    return

def switching_clock():
    return 


if __name__ == '__main__':
    C = int(input())
    for _ in range(C):
        clock_list = list(map(int, input().split()))