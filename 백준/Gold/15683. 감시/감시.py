import sys
import copy
input = sys.stdin.readline

row, col = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(row)]
cctv_type_1 = [
    [0, 1], [0, -1], [1, 0], [-1, 0]
]
cctv_type_2 = [
    [[0, 1], [0, -1]],
    [[1, 0], [-1, 0]]
]
cctv_type_3 = [
    # 위오
    [[-1, 0], [0, 1]],
    # 아오
    [[1, 0], [0, 1]],
    # 아왼
    [[0, -1], [1, 0]],
    # 위왼
    [[0, -1], [-1, 0]],
]
cctv_type_4 = [
    # 왼오위
    [[0, -1], [0, 1], [-1, 0]],
    # 위아오
    [[1, 0], [-1, 0], [0, 1]],
    # 왼오아
    [[0, -1], [1, 0], [0, 1]],
    # 위아왼
    [[1, 0], [-1, 0], [0, -1]]
]
cctv_type_5 = [[0, 1], [-1, 0], [0, -1], [1, 0]]

cctv_loc = []
wall_loc = []
for r in range(row):
    for c in range(col):
        if arr[r][c] != 0 and arr[r][c] != 6:
            cctv_loc.append([arr[r][c], (r, c)])
        elif arr[r][c] == 6:
            wall_loc.append((r, c))

ans = float('inf')

def sol(cctv_index, new_arr):
    global ans
    if cctv_index == len(cctv_loc):
        cnt = 0
        for r in range(row):
            for c in range(col):
                if new_arr[r][c] == 0:
                    cnt += 1
        if cnt < ans:
            ans = cnt
            # print('또 뭐가 문젠데...', new_arr)
        return
    else:
        sr, sc = cctv_loc[cctv_index][1][0], cctv_loc[cctv_index][1][1]
        if cctv_loc[cctv_index][0] == 1:
            for c in cctv_type_1:
                next_arr = copy.deepcopy(new_arr)
                cr, cc = sr, sc
                while True:
                    nr, nc = cr + c[0], cc + c[1]
                    if 0 <= nr < row and 0 <= nc < col and next_arr[nr][nc] != 6:
                         next_arr[nr][nc] = 'c'
                         cr, cc = nr, nc
                    else:
                        break
                sol(cctv_index + 1, next_arr)
        elif 2 <= cctv_loc[cctv_index][0] <= 4:
            cur_cctv_type = []
            if cctv_loc[cctv_index][0] == 2:
                cur_cctv_type = cctv_type_2
            elif cctv_loc[cctv_index][0] == 3:
                cur_cctv_type = cctv_type_3
            else:
                cur_cctv_type = cctv_type_4
            for c in cur_cctv_type:
                next_arr = copy.deepcopy(new_arr)
                for dir in c:
                    cr, cc = sr, sc
                    while True:
                        nr, nc = cr + dir[0], cc + dir[1]
                        if 0 <= nr < row and 0 <= nc < col and next_arr[nr][nc] != 6:
                            next_arr[nr][nc] = 'c'
                            cr, cc = nr, nc
                        else:
                            break
                # print(cctv_index, c, next_arr)
                sol(cctv_index + 1, next_arr)
        else:
            next_arr = copy.deepcopy(new_arr)
            for c in cctv_type_5:
                cr, cc = sr, sc
                while True:
                    nr, nc = cr + c[0], cc + c[1]
                    if 0 <= nr < row and 0 <= nc < col and next_arr[nr][nc] != 6:
                         next_arr[nr][nc] = 'c'
                         cr, cc = nr, nc
                    else:
                        break
            sol(cctv_index + 1, next_arr)

sol(0, arr)
print(ans)
