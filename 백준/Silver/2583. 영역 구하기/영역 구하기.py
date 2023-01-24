import sys
input = sys.stdin.readline

def sol(stack):
    global arr, area
    while stack:
        sr, sc = stack.pop()
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        for move in moves:
            nr, nc = sr + move[0], sc + move[1]
            if 0 <= nr and nr < n and 0 <= nc and nc < m and arr[nr][nc] == False:
                arr[nr][nc] = True
                area += 1
                stack.append([nr, nc])
    return area
    
n, m, k = map(int, input().split())
arr = [[False]*m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for c in range(x1, x2):
        for r in range(y1, y2):
            arr[r][c] = True


area_list = []
for r in range(n):
    for c in range(m):
        if arr[r][c] == False:
            arr[r][c] = True
            area = 1
            area_list.append(sol([[r, c]]))
area_list.sort()
print(len(area_list))
print(*area_list)