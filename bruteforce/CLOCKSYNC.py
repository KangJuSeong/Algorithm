import sys
input = sys.stdin.readline

result = 0

SWITCH = {
            0: [0, 1, 2], 1: [3, 7, 9, 11], 2: [4, 10, 14 ,15],
            3: [0, 4, 5, 6, 7], 4: [6, 7, 8, 10, 12], 5: [0, 2, 14, 15],
            6: [3, 14, 15], 7: [4, 5, 7, 14, 15], 8: [1, 2, 3, 4, 5],
            9: [3, 4, 5, 9, 13]
         }

def check_all_twelve(clock_list):
    twelve_cnt = 0
    for idx, time in enumerate(clock_list):
        if time == 12: twelve_cnt += 1
    if twelve_cnt == 16: return 1
    else: return 0

def switching_clock(clock_list, switch_num):
    global result
    if check_all_twelve(clock_list): return 0
    else:
        if switch_num >= 10:
            return sys.maxsize
        for idx, clock in enumerate(SWITCH[switch_num]):
            for cnt in range(0, 4):
                _clock_list = list(clock_list)
                print(_clock_list)
                print(clock_list)
                _clock_list[clock] += 3 * cnt
                if _clock_list[clock] >= 15:
                    _clock_list[clock] %= 12
                    if _clock_list[clock] == 0:
                        _clock_list[clock] = 12
                print(f'{switch_num} : {cnt}')
                _result = result + cnt + switching_clock(_clock_list, switch_num+1)
            return min(_result, sys.maxsize)
        # return result


if __name__ == '__main__':
    # C = int(input())
    C = 1
    for _ in range(C):
        # clock_list = list(map(int, input().split()))
        clock_list = [12,6,6,6,6,6,12,12,12,12,12,12,12,12,12,12]
        answer = switching_clock(clock_list, 0)
        if answer == sys.maxsize: print(-1)
        else: print(answer)
        result = 0
        