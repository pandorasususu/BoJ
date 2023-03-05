n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
min_length = n + 1
sum = arr[0]

while left <= right and right < n:
    if sum < s:
        right += 1
        if right < n:
            sum += arr[right]

    else:
        length = right - left + 1
        if length < min_length:
            min_length = length
        sum -= arr[left]
        left += 1

if min_length == n + 1:
    print(0)
else:
    print(min_length)