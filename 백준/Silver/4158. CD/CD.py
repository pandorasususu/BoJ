import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    ans = 0
    arr_1, arr_2 = [], []
    for _ in range(n):
        arr_1.append(int(input()))
    for _ in range(m):
        arr_2.append(int(input()))
    
    one, two = 0, 0
    while one < n and two < m:
        if arr_1[one] == arr_2[two]:
            ans += 1
            one += 1
            two += 1
        elif arr_1[one] > arr_2[two]:
            two += 1
        else:
            one += 1 
    print(ans)