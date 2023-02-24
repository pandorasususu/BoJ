import sys
from itertools import product
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = list(product(arr, repeat=m))
ans.sort()
for v in ans:
    print(*v)