import sys
input = sys.stdin.readline

n = int(input())
arr = []
max_num = 0
min_num = 100
for _ in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)
    if max_num < max(nums):
        max_num = max(nums)
    if min_num > min(nums):
        min_num = min(nums)

moves = [[1,0],[-1,0],[0,1],[0,-1]]
max_area_cnt = 1
for level in range(min_num, max_num+1):
    area_cnt = 0
    visited = [[False] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if arr[r][c] > level and visited[r][c] == False:
                area_cnt += 1
                stack = [[r,c]]
                visited[r][c] = True
                while stack:
                    sr, sc = stack.pop()
                    for move in moves:
                        nr, nc = sr + move[0], sc + move[1]
                        if 0 <= nr and nr < n and 0 <= nc and nc < n and arr[nr][nc] > level and visited[nr][nc] == False:
                            visited[nr][nc] = True
                            stack.append([nr, nc])
    if area_cnt > max_area_cnt:
        max_area_cnt = area_cnt

print(max_area_cnt)