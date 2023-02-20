import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for i in range(n):
    num = int(input())
    if num <= k:
        arr.append(num)
arr.sort()
dp = [10001] * (k+1)
dp[0] = 0
for i in arr:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)
        # if j % i == 0:
        #     dp[j] = j // i
        # else:
        #     closest = (j // i) * i
        #     dp[j] = min(dp[j], dp[closest] + dp[j-closest])

if dp[k] == 10001:
    print(-1)
else: 
    print(dp[k])