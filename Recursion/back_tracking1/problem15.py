"""
문제
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.

출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

예제 입력 1 
5 0
-7 -3 -2 5 8
예제 출력 1 
1
"""
import sys
from typing import List


cnt: int = 0


def BT(i: int, S: int, ans: List[int], arr: List[int], idx: int, n: int):
    global cnt
    if idx == i:
        if sum(ans) == S:
            cnt = cnt + 1
        return
    for k in range(n, len(arr)):
        ans[idx] = arr[k]
        BT(i, S, ans, arr, idx+1, k+1)


N, S = map(int, sys.stdin.readline().split())
arr: List[int] = list(map(int, sys.stdin.readline().split()))
for i in range(1, N+1):
    ans: List[int] = [i for i in range(i)]
    BT(i, S, ans, arr, 0, 0)
print(cnt)