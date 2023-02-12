from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
tmts = []
goals = 0
already = 0
for r in range(m):
    for c in range(n):
        if arr[r][c] == 1:
            tmts.append([r, c])
            already += 1
        elif arr[r][c] == 0:
            goals += 1
moves = [[0,1],[0,-1],[1,0],[-1,0]]
ans = 0
trials = 0
while tmts:
    new_tmts = []
    for i, v in enumerate(tmts):
        r, c = v[0], v[1]
        if visited[r][c] == False:
            visited[r][c] = True
            trials += 1
        else: continue
        for m1, m2 in moves:
            nr, nc = r + m1, c + m2
            if (nr < m and 0 <= nr) and (nc < n and 0 <= nc) and \
                (visited[nr][nc] == False) and (arr[nr][nc] != -1):
                new_tmts.append([nr, nc])
    else:
        if goals != trials - already: 
            ans += 1
        tmts = new_tmts
        # print(tmts, ans, trials)

if goals == 0:
    print(0)
elif goals != trials - already:
    print(-1)
else:
    print(ans)

