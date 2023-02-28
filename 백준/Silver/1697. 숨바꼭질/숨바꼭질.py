import sys
from collections import deque
input = sys.stdin.readline

s, e = map(int, input().split())
loc = [0] * 100001

def sol():
    q = deque()
    q.append(s)
    while q:
        x = q.popleft()
        if x == e:
            print(loc[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and not loc[i]:
                loc[i] = loc[x] + 1
                q.append(i)

sol()