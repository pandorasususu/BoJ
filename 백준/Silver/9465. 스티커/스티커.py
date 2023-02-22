import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for __ in range(2)]
    visited = [[0] * n for __ in range(2)]
    visited[0][0] = arr[0][0]
    visited[1][0] = arr[1][0]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    else:
        for i in range(1, n):
            visited[0][i] = max(visited[1][i-1] + arr[0][i], visited[0][i-1])
            visited[1][i] = max(visited[0][i-1] + arr[1][i], visited[1][i-1])
        print(max(visited[0][n-1], visited[1][n-1]))