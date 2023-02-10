from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[0][0] = arr[0][0]
for r in range(n):
    for c in range(m):
        sr, sc = r, c
        moves = [[1,0],[0,1],[1,1]]
        for move in moves:
            nr, nc = sr + move[0], sc + move[1]
            if nr < n and nc < m:
                visited[nr][nc] = max(visited[sr][sc] + arr[nr][nc], visited[nr][nc])

print(visited[n-1][m-1])