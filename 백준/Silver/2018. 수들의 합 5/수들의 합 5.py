import sys
input = sys.stdin.readline

n = int(input())
def sol():
    ans = 1
    left, right = n // 2, (n // 2) + 1
    sum = left + right
    cnt = 0
    while 0 <= left and left < right:
        cnt += 1
        if sum == n:
            ans += 1
            # print(left, right)
            right -= 1
            left = right - 1
            sum = left + right
        elif sum > n:
            right -= 1
            left = right - 1
            sum = left + right
            
        else:
            left -= 1
            sum += left
    # print(cnt)
    if n == 1:
        ans = 1
    return ans

print(sol())    