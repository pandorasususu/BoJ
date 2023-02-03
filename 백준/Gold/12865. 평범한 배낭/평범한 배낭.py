from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
knapsack = [[0] * (k+1) for _ in range(n+1)]
for i in range(n):
    for j in range(1, k+1):
        w, v = arr[i][0], arr[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[n-1][k])