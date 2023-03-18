import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
x = int(input())

cnt = 0
left, right = 0, n - 1
sum = arr[left] + arr[right]

while left < right:
    if sum > x:
        sum -= arr[right] 
        right -= 1
        sum += arr[right]
    elif sum < x:
        sum -= arr[left]
        left += 1
        sum += arr[left]
    else:
        cnt += 1
        sum -= (arr[left] + arr[right])
        right -= 1
        left += 1
        sum += (arr[left] + arr[right])

print(cnt)