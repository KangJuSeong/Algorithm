import sys

input = sys.stdin.readline
global cnt
cnt = 0

def DFS(pair_cnt, real_friend, i, student):
    global cnt
    if pair_cnt == 0:
        cnt += 1
        return
    if i >= len(real_friend):
        return
    tup = real_friend[i]
    if tup[0] in student or tup[1] in student:
        DFS(pair_cnt, real_friend, i+1, student)
    else:
        if len(student) >= 2:
            _student = student[:]
            DFS(pair_cnt, real_friend, i+1, _student)
        student.append(tup[0])
        student.append(tup[1])
        DFS(pair_cnt-1, real_friend, i+1, student)

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        friend = list(map(int, input().split()))
        real_friend = []
        for i in range(0, m*2, 2):
            real_friend.append((friend[i], friend[i+1]))
        pair_cnt = int(n / 2)
        for i in range(0, len(real_friend)):
            DFS(pair_cnt, real_friend, i, [])
        print(cnt)
        cnt = 0
