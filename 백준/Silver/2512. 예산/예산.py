import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
budget = int(input())
start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2
    total_budget = 0

    for a in arr:
        total_budget += min(mid, a)
    if total_budget > budget:
        end = mid - 1
    else:
        start = mid + 1
print(end)