import sys
from bisect import bisect_left
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
def sol():
    ans = float('inf')
    for i, v in enumerate(arr):
        cnd_index = bisect_left(arr, v + m)
        cnd_list = [] 
        if 1 <= cnd_index < n - 1:
            cnd_list = [cnd_index - 1, cnd_index, cnd_index + 1]
        elif cnd_index == 0:
            cnd_list = [cnd_index, cnd_index + 1]
        elif cnd_index == n - 1:
            cnd_list = [cnd_index, cnd_index - 1]
        # print(cnd_index, cnd_list, v)
        for elem in cnd_list:
            if arr[elem] - v >= m and ans > arr[elem] - v:
                ans = arr[elem] - v
            
    return ans
print(sol())