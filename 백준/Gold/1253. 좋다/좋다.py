import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
def sol():
    ans = 0
    for i, v in enumerate(arr):
        left, right = 0, n - 1
        while left < right:
            if right == i:
                right -= 1
            if left == i:
                left += 1
            if right == left:
                break
            sum_val = arr[left] + arr[right]
            # print(v, sum_val, arr[left], arr[right])
            if sum_val > v:
                right -= 1
                # if right == i:
                #     right -= 1
                sum_val = arr[left] + arr[right]
            elif sum_val < v:
                left += 1
                # if left == i:
                #     left += 1
                sum_val = arr[left] + arr[right]
            else:
                ans += 1
                # print(v, arr[left], arr[right])
                break
    return ans

print(sol())    