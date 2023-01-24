import sys
from pprint import pprint
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

def sol(stack):
    global visited, area
    while stack:
        sr, sc = stack.pop()
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        for move in moves:
            nr, nc = sr + move[0], sc + move[1]
            if 0 <= nr and nr < n and 0 <= nc and nc < m and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                area += 1
                stack.append([nr, nc])
            # if nr < 0 or nr >= n or nc < 0 or nc >= m:
            #     continue 
            # if arr[nr][nc] != 0 or visited[nr][nc] != 0:
            #     continue
            # visited[nr][nc] = 1
            # area += 1
            # stack.append([nr, nc])
    return area
    
n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for c in range(x1, x2):
        for r in range(y1, y2):
            arr[r][c] = 1


area_list = []
for r in range(n):
    for c in range(m):
        if arr[r][c] == 0 and visited[r][c] == 0:
            visited[r][c] = 1
            area = 1
            area_list.append(sol([[r, c]]))
area_list.sort()
print(len(area_list))
print(*area_list)