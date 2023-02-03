from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
dp = [0] * (k+1)

for w, v in arr:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i-w] + v, dp[i])

print(dp[k])