import sys
from bisect import bisect_left
input = sys.stdin.readline

t = int(input())
arr1, arr2 = list(map(int, input().split())), list(map(int, input().split()))
def sol(arr1, arr2):
    dict1 = {v: i for i, v in enumerate(arr1)}
    indices = []
    for elem in arr2:
        if elem in dict1:
            indices.append(dict1[elem])
    LIS = []
    for index in indices:
        pos = bisect_left(LIS, index)
        if pos == len(LIS):
            LIS.append(index)
        else:
            LIS[pos] = index
    return len(LIS)
print(sol(arr1, arr2))