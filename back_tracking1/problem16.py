"""
문제
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.

출력
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.

예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
"""
import sys


cnt = 0


def BT(ans, i, k, n):
    global cnt
    if i == k:
        if sum(ans) == n:
            # print("+".join(map(str, ans)))
            cnt += 1
        return
    for j in range(1, 4):
        ans[k] = j
        BT(ans, i, k+1, n)


T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    for i in range(1, n+1):
        ans = [0 for _ in range(i)]
        BT(ans, i, 0, n)
    print(cnt)
    cnt = 0