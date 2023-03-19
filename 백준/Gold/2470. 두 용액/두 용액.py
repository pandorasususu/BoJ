import sys
# from collections import deque
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
def sol():
    min_diff = float('inf')
    ans = []
    for i, v in enumerate(arr):
        cnd_index = bisect_left(arr, -v)
        cnd_list = []
        if 1 <= cnd_index < n - 1:
            cnd_list = [cnd_index - 1, cnd_index, cnd_index + 1]
        elif cnd_index == 0:
            cnd_list = [cnd_index, cnd_index + 1]
        elif cnd_index == n - 1:
            cnd_list = [cnd_index, cnd_index - 1]
        elif cnd_index == n:
            cnd_list = [cnd_index - 1]
        # print(cnd_list)
        for e in cnd_list:
            if e == i:
                continue
            if abs(arr[e] + v) < min_diff:
                min_diff = abs(arr[e] + v) 
                ans = [arr[e], v]
    return sorted(ans)
print(*sol())