"""
self number
"""


if "__main__" == __name__:
    arr: list = [0 for _ in range(10000)]
    for i in range(10000, -1, -1):
        num_arr: list = [int(num) for num in str(i)]
        num_arr.append(i)
        num_sum: int = sum(num_arr)
        if num_sum != 0 and num_sum <= 10000:
            arr[num_sum-1] = 1
    for i, v in enumerate(arr):
        if not v:
            print(i+1)
