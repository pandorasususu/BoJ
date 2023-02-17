import sys 
import heapq
input = sys.stdin.readline
cnt = 0
while True:
    cnt += 1
    m = int(input())
    if m == 0: break
    arr = [list(map(int, input().split())) for _ in range(m)]
    visited = [[float('inf')] * m for _ in range(m)]
    visited[0][0] = arr[0][0]
    moves = [(0,1),(0,-1),(1,0),(-1,0)]

    q = []
    heapq.heappush(q, (arr[0][0], (0,0)))
    while q:
        val, node = heapq.heappop(q)
        sr, sc = node[0], node[1]
        for move in moves:
            nr, nc = sr + move[0], sc + move[1]
            if 0 <= nr and nr < m and 0 <= nc and nc < m:
                if visited[nr][nc] > visited[sr][sc] + arr[nr][nc]:
                    visited[nr][nc] = visited[sr][sc] + arr[nr][nc]
                    heapq.heappush(q, (visited[nr][nc], (nr, nc)))

    print(f'Problem {cnt}: {visited[m-1][m-1]}')