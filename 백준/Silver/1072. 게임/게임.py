import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x
start, end = 1, 1000000000

if z >= 99:
    print(-1)
else:
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        next = (y + mid) * 100 // (x + mid)
        if next > z:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    print(ans)
