import sys
input = sys.stdin.readline

def dfs(w, h, stack):
    moves = [
        [-1,-1],
        [-1,0],
        [-1,1],
        [0,-1],
        [0,0],
        [0,1],
        [1,-1],
        [1,0],
        [1,1],
    ]
    while stack:
        sr, sc = stack.pop()
        for move in moves:
            nr, nc = sr + move[0], sc + move[1]
            if 0 <= nr and nr < h and 0 <= nc and nc < w and arr[nr][nc] == 1:
                arr[nr][nc] = 0 
                stack.append([nr, nc])
    return
while True:
    w, h = map(int, input().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    # print(arr)
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1:
                arr[r][c] = 0
                cnt += 1
                dfs(w, h, [[r,c]])
    print(cnt)