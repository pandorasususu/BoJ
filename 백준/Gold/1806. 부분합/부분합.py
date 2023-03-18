import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
min_len = n + 1
sum = arr[0]
while left <= right and right < n:
    if sum < s:
        right += 1
        if right < n:
            sum += arr[right]
    else:
        cur_len = right - left + 1
        if cur_len < min_len:
            min_len = cur_len
        sum -= arr[left]
        left += 1
if min_len == n + 1:
    print(0)
else:
    print(min_len)
