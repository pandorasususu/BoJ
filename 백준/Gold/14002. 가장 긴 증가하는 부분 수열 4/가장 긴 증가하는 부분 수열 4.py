import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

# 1. DP 리스트 초기화
dp = [1] * n

# 2. DP 알고리즘
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

# 3. 최대 길이 찾기
max_len = max(dp)

# 4. 부분 수열 찾기
result = []
for i in range(n-1, -1, -1):
    if dp[i] == max_len:
        result.append(a[i])
        max_len -= 1
result.reverse()

print(len(result))
print(" ".join(map(str, result)))